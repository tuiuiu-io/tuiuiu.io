from __future__ import absolute_import, unicode_literals

import json

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render

from tuiuiu.utils.pagination import paginate
from tuiuiu.tuiuiuadmin.forms import SearchForm
from tuiuiu.tuiuiuadmin.modal_workflow import render_modal_workflow
from tuiuiu.tuiuiuadmin.utils import PermissionPolicyChecker
from tuiuiu.tuiuiucore import hooks
from tuiuiu.tuiuiucore.models import Collection
from tuiuiu.tuiuiudocs.forms import get_document_form
from tuiuiu.tuiuiudocs.models import get_document_model
from tuiuiu.tuiuiudocs.permissions import permission_policy
from tuiuiu.tuiuiusearch import index as search_index

permission_checker = PermissionPolicyChecker(permission_policy)


def get_document_json(document):
    """
    helper function: given a document, return the json to pass back to the
    chooser panel
    """

    return json.dumps({
        'id': document.id,
        'title': document.title,
        'url': document.url,
        'edit_link': reverse('tuiuiudocs:edit', args=(document.id,)),
    })


def chooser(request):
    Document = get_document_model()

    if permission_policy.user_has_permission(request.user, 'add'):
        DocumentForm = get_document_form(Document)
        uploadform = DocumentForm(user=request.user)
    else:
        uploadform = None

    documents = Document.objects.all()

    # allow hooks to modify the queryset
    for hook in hooks.get_hooks('construct_document_chooser_queryset'):
        documents = hook(documents, request)

    q = None
    if 'q' in request.GET or 'p' in request.GET or 'collection_id' in request.GET:

        collection_id = request.GET.get('collection_id')
        if collection_id:
            documents = documents.filter(collection=collection_id)

        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            q = searchform.cleaned_data['q']

            documents = documents.search(q)
            is_searching = True
        else:
            documents = documents.order_by('-created_at')
            is_searching = False

        # Pagination
        paginator, documents = paginate(request, documents, per_page=10)

        return render(request, "tuiuiudocs/chooser/results.html", {
            'documents': documents,
            'query_string': q,
            'is_searching': is_searching,
        })
    else:
        searchform = SearchForm()

        collections = Collection.objects.all()
        if len(collections) < 2:
            collections = None

        documents = documents.order_by('-created_at')
        paginator, documents = paginate(request, documents, per_page=10)

        return render_modal_workflow(request, 'tuiuiudocs/chooser/chooser.html', 'tuiuiudocs/chooser/chooser.js', {
            'documents': documents,
            'uploadform': uploadform,
            'searchform': searchform,
            'collections': collections,
            'is_searching': False,
        })


def document_chosen(request, document_id):
    document = get_object_or_404(get_document_model(), id=document_id)

    return render_modal_workflow(
        request, None, 'tuiuiudocs/chooser/document_chosen.js',
        {'document_json': get_document_json(document)}
    )


@permission_checker.require('add')
def chooser_upload(request):
    Document = get_document_model()
    DocumentForm = get_document_form(Document)

    if request.method == 'POST':
        document = Document(uploaded_by_user=request.user)
        form = DocumentForm(request.POST, request.FILES, instance=document, user=request.user)

        if form.is_valid():
            form.save()

            # Reindex the document to make sure all tags are indexed
            search_index.insert_or_update_object(document)

            return render_modal_workflow(
                request, None, 'tuiuiudocs/chooser/document_chosen.js',
                {'document_json': get_document_json(document)}
            )
    else:
        form = DocumentForm(user=request.user)

    documents = Document.objects.order_by('title')

    return render_modal_workflow(
        request, 'tuiuiudocs/chooser/chooser.html', 'tuiuiudocs/chooser/chooser.js',
        {'documents': documents, 'uploadform': form}
    )
