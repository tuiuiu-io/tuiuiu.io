from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from tuiuiu.tuiuiuadmin.userbar import (
    AddPageItem, ApproveModerationEditPageItem, EditPageItem, RejectModerationEditPageItem)
from tuiuiu.tuiuiucore import hooks
from tuiuiu.tuiuiucore.models import Page, PageRevision


@permission_required('tuiuiuadmin.access_admin', raise_exception=True)
def for_frontend(request, page_id):
    items = [
        EditPageItem(Page.objects.get(id=page_id)),
        AddPageItem(Page.objects.get(id=page_id)),
    ]

    for fn in hooks.get_hooks('construct_tuiuiu_userbar'):
        fn(request, items)

    # Render the items
    rendered_items = [item.render(request) for item in items]

    # Remove any unrendered items
    rendered_items = [item for item in rendered_items if item]

    # Render the edit bird
    return render(request, 'tuiuiuadmin/userbar/base.html', {
        'items': rendered_items,
    })


@permission_required('tuiuiuadmin.access_admin', raise_exception=True)
def for_moderation(request, revision_id):
    items = [
        EditPageItem(PageRevision.objects.get(id=revision_id).page),
        AddPageItem(PageRevision.objects.get(id=revision_id).page),
        ApproveModerationEditPageItem(PageRevision.objects.get(id=revision_id)),
        RejectModerationEditPageItem(PageRevision.objects.get(id=revision_id)),
    ]

    for fn in hooks.get_hooks('construct_tuiuiu_userbar'):
        fn(request, items)

    # Render the items
    rendered_items = [item.render(request) for item in items]

    # Remove any unrendered items
    rendered_items = [item for item in rendered_items if item]

    # Render the edit bird
    return render(request, 'tuiuiuadmin/userbar/base.html', {
        'items': rendered_items,
    })
