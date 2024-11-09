from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
import math

class AdvancedCalculatorApp(App):
    def build(self):
        # إعدادات النافذة
        Window.clearcolor = (0.95, 0.95, 0.97, 1)
        
        # التخطيط الرئيسي
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # شاشة العرض الرئيسية
        self.display = TextInput(
            multiline=False, 
            readonly=True, 
            size_hint_y=0.2,  # تكبير الشاشة
            font_size=dp(40),
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            halign='right',
            padding=[dp(15), dp(10)]
        )
        main_layout.add_widget(self.display)
        
        # شاشة العمليات
        self.operations_display = TextInput(
            multiline=False, 
            readonly=True, 
            size_hint_y=0.1,  # شاشة للعمليات
            font_size=dp(20),
            background_color=(0.95, 0.95, 0.97, 1),
            foreground_color=(0.5, 0.5, 0.5, 1),
            halign='right',
            padding=[dp(15), dp(10)]
        )
        main_layout.add_widget(self.operations_display)
        
        # مجموعة الأزرار العلمية والأساسية
        scientific_buttons = [
            ['sin', 'cos', 'tan', 'log', 'ln'],
            ['√', '^', '(', ')', 'C']
        ]
        
        basic_buttons = [
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        # إضافة الأزرار العلمية
        for row in scientific_buttons:
            row_layout = BoxLayout(spacing=dp(5), size_hint_y=None, height=dp(50))
            for label in row:
                btn = self.create_button(label, 'scientific')
                row_layout.add_widget(btn)
            main_layout.add_widget(row_layout)
        
        # إضافة الأزرار الأساسية
        for row in basic_buttons:
            row_layout = BoxLayout(spacing=dp(5), size_hint_y=None, height=dp(50))
            for label in row:
                btn = self.create_button(label, 'basic')
                row_layout.add_widget(btn)
            main_layout.add_widget(row_layout)
        
        return main_layout
    
    def create_button(self, text, button_type):
        # إنشاء زر بتصميم عصري
        btn = Button(
            text=text,
            font_size=dp(18),  # تصغير حجم الخط
            background_color=(0, 0, 0, 0)
        )
        
        # تحديد لون الزر حسب النوع
        if button_type == 'scientific':
            btn.color = (0.2, 0.6, 0.8, 1)  # أزرق فاتح للعمليات العلمية
        else:
            btn.color = (0.2, 0.2, 0.2, 1)  # رمادي للأزرار الأساسية
        
        # تخصيص مظهر الزر
        btn.bind(pos=self.update_button_canvas, size=self.update_button_canvas)
        btn.bind(on_press=self.on_button_press)
        return btn
    
    def update_button_canvas(self, instance, *args):
        # تحديث تصميم الأزرار
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            RoundedRectangle(
                pos=instance.pos, 
                size=instance.size, 
                radius=[dp(8)]
            )
    
    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text
        
        try:
            if button_text == 'C':
                # مسح الشاشة
                self.display.text = ''
                self.operations_display.text = ''
            elif button_text == '=':
                # حساب النتيجة
                try:
                    # معالجة العمليات العلمية
                    if 'sin' in current:
                        result = math.sin(float(current.replace('sin', '')))
                    elif 'cos' in current:
                        result = math.cos(float(current.replace('cos', '')))
                    elif 'tan' in current:
                        result = math.tan(float(current.replace('tan', '')))
                    elif 'log' in current:
                        result = math.log10(float(current.replace('log', '')))
                    elif 'ln' in current:
                        result = math.log(float(current.replace('ln', '')))
                    elif '√' in current:
                        result = math.sqrt(float(current.replace('√', '')))
                    else:
                        result = eval(
                            current.replace('÷', '/').replace('×', '*').replace('^', '**')
                        )
                    
                    self.display.text = str(result)
                    self.operations_display.text = current + ' = '
                except Exception as e:
                    self.display.text = 'خطأ'
            else:
                # إضافة الأرقام والعمليات
                self.display.text += button_text
        except Exception:
            self.display.text = 'خطأ'

def main():
    AdvancedCalculatorApp().run()

if __name__ == '__main__':
    main()from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
import math

class AdvancedCalculatorApp(App):
    def build(self):
        # إعدادات النافذة
        Window.clearcolor = (0.95, 0.95, 0.97, 1)
        
        # التخطيط الرئيسي
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # شاشة العرض الرئيسية
        self.display = TextInput(
            multiline=False, 
            readonly=True, 
            size_hint_y=0.2,  # تكبير الشاشة
            font_size=dp(40),
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            halign='right',
            padding=[dp(15), dp(10)]
        )
        main_layout.add_widget(self.display)
        
        # شاشة العمليات
        self.operations_display = TextInput(
            multiline=False, 
            readonly=True, 
            size_hint_y=0.1,  # شاشة للعمليات
            font_size=dp(20),
            background_color=(0.95, 0.95, 0.97, 1),
            foreground_color=(0.5, 0.5, 0.5, 1),
            halign='right',
            padding=[dp(15), dp(10)]
        )
        main_layout.add_widget(self.operations_display)
        
        # مجموعة الأزرار العلمية والأساسية
        scientific_buttons = [
            ['sin', 'cos', 'tan', 'log', 'ln'],
            ['√', '^', '(', ')', 'C']
        ]
        
        basic_buttons = [
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        # إضافة الأزرار العلمية
        for row in scientific_buttons:
            row_layout = BoxLayout(spacing=dp(5), size_hint_y=None, height=dp(50))
            for label in row:
                btn = self.create_button(label, 'scientific')
                row_layout.add_widget(btn)
            main_layout.add_widget(row_layout)
        
        # إضافة الأزرار الأساسية
        for row in basic_buttons:
            row_layout = BoxLayout(spacing=dp(5), size_hint_y=None, height=dp(50))
            for label in row:
                btn = self.create_button(label, 'basic')
                row_layout.add_widget(btn)
            main_layout.add_widget(row_layout)
        
        return main_layout
    
    def create_button(self, text, button_type):
        # إنشاء زر بتصميم عصري
        btn = Button(
            text=text,
            font_size=dp(18),  # تصغير حجم الخط
            background_color=(0, 0, 0, 0)
        )
        
        # تحديد لون الزر حسب النوع
        if button_type == 'scientific':
            btn.color = (0.2, 0.6, 0.8, 1)  # أزرق فاتح للعمليات العلمية
        else:
            btn.color = (0.2, 0.2, 0.2, 1)  # رمادي للأزرار الأساسية
        
        # تخصيص مظهر الزر
        btn.bind(pos=self.update_button_canvas, size=self.update_button_canvas)
        btn.bind(on_press=self.on_button_press)
        return btn
    
    def update_button_canvas(self, instance, *args):
        # تحديث تصميم الأزرار
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            RoundedRectangle(
                pos=instance.pos, 
                size=instance.size, 
                radius=[dp(8)]
            )
    
    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text
        
        try:
            if button_text == 'C':
                # مسح الشاشة
                self.display.text = ''
                self.operations_display.text = ''
            elif button_text == '=':
                # حساب النتيجة
                try:
                    # معالجة العمليات العلمية
                    if 'sin' in current:
                        result = math.sin(float(current.replace('sin', '')))
                    elif 'cos' in current:
                        result = math.cos(float(current.replace('cos', '')))
                    elif 'tan' in current:
                        result = math.tan(float(current.replace('tan', '')))
                    elif 'log' in current:
                        result = math.log10(float(current.replace('log', '')))
                    elif 'ln' in current:
                        result = math.log(float(current.replace('ln', '')))
                    elif '√' in current:
                        result = math.sqrt(float(current.replace('√', '')))
                    else:
                        result = eval(
                            current.replace('÷', '/').replace('×', '*').replace('^', '**')
                        )
                    
                    self.display.text = str(result)
                    self.operations_display.text = current + ' = '
                except Exception as e:
                    self.display.text = 'خطأ'
            else:
                # إضافة الأرقام والعمليات
                self.display.text += button_text
        except Exception:
            self.display.text = 'خطأ'

def main():
    AdvancedCalculatorApp().run()

if __name__ == '__main__':
    main()