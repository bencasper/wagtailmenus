from __future__ import absolute_import, unicode_literals

from django.db import models


class MenuItemManager(models.Manager):
    ''' App-specific manager overrides '''

    def for_display(self):
        return self.filter(
            models.Q(link_page__isnull=True) |
            models.Q(link_page__live=True) &
            models.Q(link_page__expired=False) &
            models.Q(link_page__show_in_menus=True)
        )
