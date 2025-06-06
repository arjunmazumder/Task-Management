from django import forms
from tasks.models import Task, TaskDetail
#Django Form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label='Task Title')
    description = forms.CharField(widget=forms.Textarea, label='Task description')
    due_date = forms.DateField(label="Due date", widget=forms.SelectDateWidget)
    assignedTo = forms.MultipleChoiceField(
        label='Assign To', widget=forms.CheckboxSelectMultiple, choices=[])

    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        super().__init__(*args, **kwargs)
        self.fields['assignTo'].choices=[(emp.id, emp.name) for emp in employees]

#Mixin class        
class StyledFormMixin:
    """mixin to apply style to form field"""
    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-nome focus:border-rose-500",
    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update(
                    {
                        'class' : self.default_classes,
                        'placeholder' : f"Enter {field.label.lower()}"
                    }    
                )
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update(
                    {
                        'class' : self.default_classes,
                        'placeholder' : f"Enter {field.label.lower()}",
                        'rows' : 5
                    }
                )
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update(
                    {
                        'class' : 'border-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-nome focus:border-rose-500',
                        
                    }
                )
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update(
                    {
                        'class' : "space-y-2"
                    }
                )
            else:
                
                field.widget.attrs.update(
                    {
                        'class':self.default_classes
                    }
                )

#Task_models_form
class TaskModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','assignedTo']
        widgets = {
            'title' : forms.TextInput,
            'descirption' : forms.Textarea,
            'due_date' : forms.SelectDateWidget,
            'assignedTo' : forms.CheckboxSelectMultiple
        }

    '''Using mixin widget'''  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

#Task_Details_Model_Form
class TaskDetailModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model=TaskDetail
        fields = ['priority','notes']
        widgets = {
            # 'priority' : forms.TextInput,
            'notes' : forms.Textarea,
            # 'priority' : forms.SelectDateWidget,
            # 'priority' : forms.CheckboxSelectMultiple
        }
    

    '''Using mixin widget'''  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()



