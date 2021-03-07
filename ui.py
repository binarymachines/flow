#!/usr/bin/env python

from snap import common
import jinja2


from abc import ABC, abstractmethod, abstractproperty


class UIObject(object):
    def __init__(self, id, **attributes):
        self.id = id
        self._attributes = attributes

    
    @abstractproperty
    def element(self):
        pass

    @property
    def template(self):
        return '''
        <{{element}}
            {%- for name, value in attrs.items() %}
                {{ name }}="{{ value }}"       
            {%- endfor -%}>
        </{{element}}>
        '''

    @property
    def attributes(self):
        data = {
            'id': self.id
        }
        data.update(self._attributes)
        
        return data


    def render(self):
        j2env = jinja2.Environment()
        template_mgr = common.JinjaTemplateManager(j2env)
        j2template = j2env.from_string(self.template)
        return j2template.render(element=self.element,
                                 attrs=self._attributes)


class UIForm(object):
    def __init__(self):
        pass

    
class UIContainer(ABC):
    def __init__(self, id, label, **attributes):
        self.id = id
        self.label = label
        self.attributes = attributes
        self.components = []


    @abstractproperty
    def element(self):
        pass

    @property
    def element_attrs(self):
        data = {
            'id': self.id
        }
        data.update(self.attributes)

        return data


    @property
    def template(self):
        return '''
        <{{element}}
            {%- for name, value in attributes.items() %}
                {{ name }}="{{ value }}"       
            {%- endfor -%}
        >
            
            {% for c in components %}
                {{ c.render() }}
            {% endfor %}
            
        </{{element}}>
        '''

    @property
    def params(self) -> dict:
        return {
            'element': self.element,
            'attributes': self.element_attrs,
            'components': self.components
        }


    def render(self):        
        j2env = jinja2.Environment()
        template_mgr = common.JinjaTemplateManager(j2env)
        j2template = j2env.from_string(self.template)

        return j2template.render(**self.params)

    
    def add_component(self, ui_object: UIObject):
        self.components.append(ui_object)


class FormGroup(UIContainer):
    def __init__(self, id, label, **attributes):
        super().__init__(id, label, **attributes)

    @property
    def element(self):
        return 'b-form-group'


class FormInput(UIObject):
    def __init__(self, id, **attributes):
        super().__init__(id, **attributes)

    @property
    def element(self):
        return 'b-form-input'


class FormSelect(UIObject):
    def __init__(self, id, *options, **attributes):
        super().__init__(id, **attributes)
        self.options = options


    @property
    def element(self):
        return 'b-form-select'

    
class FormCheckboxGroup(UIObject):
    def __init__(self, id, **attributes):
        super().__init__(id, **attributes)

    @property
    def element(self):
        return 'b-form-checkbox-group'
 


class FormCheckbox(UIObject):
    def __init__(self, id, value, **attributes):
        super().__init__(id, **attributes)
        self.attributes['value'] = value

