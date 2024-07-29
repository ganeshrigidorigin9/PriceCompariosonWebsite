from flask import Flask,render_template,request
from amazon import amazon_details
from flipkart import flipkart_details
from croma import croma_details
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def product():
    product_name=''
    if request.method == 'GET':
        return render_template('product.html')
    product_name=request.form.get('name')
    amazon_list=amazon_details(product_name)
    flipkart_list=flipkart_details(product_name)
    croma_list=croma_details(product_name)
    return render_template('product.html',al=amazon_list,pn=product_name,fl=flipkart_list,cr=croma_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__=="__main__":
    app.run(debug=True)
