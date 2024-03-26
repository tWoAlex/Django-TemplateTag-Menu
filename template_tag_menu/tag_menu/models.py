from django.db import models


class Menu(models.Model):
    name = models.CharField(verbose_name='Меню',
                            max_length=100,
                            db_index=True,
                            unique=True,
                            blank=False, null=False)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return f'({self.id}) {self.name}'


class MenuItem(models.Model):
    menu = models.ForeignKey(verbose_name='Меню',
                             to=Menu, related_name='items',
                             on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название пункта',
                            max_length=100,
                            blank=False, null=False)
    parent = models.ForeignKey(verbose_name='Родительский пункт',
                               to='self', related_name='children',
                               on_delete=models.CASCADE,
                               blank=True, null=True, default=None)
    url = models.CharField(verbose_name='Прямой или именованный URL',
                           max_length=100,
                           blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

        constraints = (
            models.UniqueConstraint(
                fields=('parent', 'name'),
                name='unique_item_for_each_parent'
            ),
            models.CheckConstraint(
                check=~models.Q(id=models.F('parent')),
                name='not_self_parent'
            )
        )

    def __str__(self) -> str:
        if self.parent:
            return f'{str(self.parent)}. {self.name}'
        return f'{self.menu.name}. {self.name}'
