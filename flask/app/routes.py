from flask import render_template
from app import app
from fwd import FrontWrap
import translate
#from translate import Translate
from app.forms import GenerateForm
import argparse

# Test
parser = argparse.ArgumentParser(
            description='translate.py',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#self.opt = parser.parse_args()
# Test

textgen = FrontWrap()
#model = Translate()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = GenerateForm()
    data = []
    results = ""
    if form.validate_on_submit():       
        temp = textgen.run_fwd(form.area_text.data)
        #temp = model.forward()
        data = textgen.gen_qs()
        results = "Questions:"
    return render_template('index.html', title='Generate Questions', form=form, data=data, results=results)
    
@app.route('/about')
def generate():
    return render_template('about.html', title='About')
