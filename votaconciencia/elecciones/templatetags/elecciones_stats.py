from django import template

register = template.Library()


class PorcentajeNode(template.Node):
    def __init__(self, parcial, total):
        self.parcial = template.Variable(parcial)
        self.total = template.Variable(total)

    def render(self, context):
        parcial = self.parcial.resolve(context)
        total = self.total.resolve(context)
        return "%.2f %%" % (float(parcial) / float(total) * 100.0)


@register.tag
def porcentaje(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, parcial, total = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires correct arguments. You passed %s and %s " % (token.contents.split()[0], token.contents.split()[1], token.contents.split()[2])
        )
    return PorcentajeNode(parcial, total)

