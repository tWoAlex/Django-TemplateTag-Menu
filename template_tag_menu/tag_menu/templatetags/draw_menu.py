from collections import namedtuple

from django import template
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from tag_menu.models import Menu, MenuItem


render_menu_item = namedtuple(
    'render_menu_item',
    ('name', 'indent', 'href')
)


def menu_items_to_tree(
        menu: list[MenuItem],
        searched_url: str, searched_name: str,
        parent: MenuItem = None, depth: int = 0, indent: str = ' ' * 3
) -> tuple[list[render_menu_item], bool]:
    def href_from_menu_item(item: MenuItem) -> str:
        try:
            href = reverse(item.url)
        except NoReverseMatch:
            href = item.url
        return href

    def has_searched_url(item: MenuItem) -> bool:
        return (item.url == searched_url
                or item.url == searched_name)

    children = [item for item in menu if item.parent == parent]
    if not len(children):
        return children, False
    children = sorted(children, key=lambda x: x.name)

    result = list()
    on_this_level = False
    for index, child in enumerate(children, start=1):
        href = href_from_menu_item(child)
        result.append(
            render_menu_item(
                name=child.name,
                indent=(f'{indent * depth}'
                        f'{"└─ " if (index == len(children)) else "├─ "}'),
                href=href
            )
        )

        its_children, in_children = menu_items_to_tree(
            menu, searched_url, searched_name,
            child, depth + 1, indent
        )
        if has_searched_url(child) or in_children:
            on_this_level = True
            result.extend(its_children)
    return result, on_this_level


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: template.context.RequestContext,
              menu_name: str) -> dict[str, list[MenuItem]]:
    searched_url = context.request.get_host() + context.request.path
    searched_name = context.request.resolver_match.url_name
    menu: list[MenuItem] = Menu.objects.get(name=menu_name).items.all()
    menu, found = menu_items_to_tree(
        menu, str(searched_url), searched_name)
    return {'menu_items': menu}
