# Copyright (c) 2016 The Pycroft Authors. See the AUTHORS file.
# This file is part of the Pycroft project and licensed under the terms of
# the Apache License, Version 2.0. See the LICENSE file for details.
from web.form.widgets import LazyLoadSelectWidget,\
    BootstrapFormControlDecorator, BootstrapStandardDecorator, \
    BootstrapFormGroupDecorator, decorate, BootstrapStaticFieldWidget, \
    decorators, decorate_field, Disabler
from wtforms import TextField, StringField
from wtforms import fields


def static(field):
    widget = field.kwargs.get("widget", field.field_class.widget)
    field.kwargs["widget"] = decorate(
        BootstrapStaticFieldWidget(),
        *reversed(list(decorators(widget)))
    )
    return field


def disabled(field):
    widget = field.kwargs.get("widget", field.field_class.widget)
    field.kwargs["widget"] = Disabler(widget)
    return field


class LazyLoadSelectField(fields.SelectField):
    """This is a select field that loads data lazy if a dependency changes

    Its used for example for the room selection:
    The levels are loaded if you select a building. The room numbers are
    loaded for the selected building and level.

    It needs a data endpoint that provides a json object with at least one
    element: "items". This stores a list of items. The item can be either a
    simple string - then the value of the generated <option> element is the
    same as its label or a array of two elements: [value, label].

    The request is a get xhr request sending the dependency values as url
    arguments. A sample implementation can be:

        @bp.route('/json/levels')
        def json_levels():
            if not request.is_xhr:
                abort(404)
            building_id = request.args.get('building', 0, type=int)
            [...]
            return jsonify(dict(items=[entry.level for entry in levels]))

    The get arguments has the same name as the id of the dependency.

    As widget the LazyLoadSelectWidget is used. It renders everything
    automatically. You need only the form.js and the initializing js code:
        <script type="text/javascript" src="{{ url_for("static", filename="custom/js/form.js") }}"></script>
        <script type="text/javascript">
            $('[data-role=lazyloadselect]').lazyLoadSelect()
        </script>

    :param conditions: The names of the fields this one depends on as a List.
    :param data_endpoint: The name of the endpoint that provides the data.
    """

    widget = decorate(
        LazyLoadSelectWidget(),
        BootstrapFormControlDecorator,
        BootstrapStandardDecorator,
        BootstrapFormGroupDecorator
    )

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs.pop("conditions")
        self.data_endpoint = kwargs.pop("data_endpoint")

        super(LazyLoadSelectField, self).__init__(*args, **kwargs)

    def pre_validate(self, form):
        pass


class TypeaheadField(StringField):
    """A Twitter typeahead.js field."""

    widget = decorate_field(
        StringField,
        BootstrapFormControlDecorator,
        BootstrapStandardDecorator,
        BootstrapFormGroupDecorator
    )

    def __call__(self, **kwargs):
        return super(TypeaheadField, self).__call__(
            class_='typeahead', **kwargs
        )


class ReadonlyTextField(TextField):
    def __call__(self, **kwargs):
        return self.widget(self, disabled=True)
