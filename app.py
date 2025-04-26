from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'dev-key-for-development'  # For flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        # For now, just flash a success message
        flash('Your message has been sent! We will get back to you soon.')
        return redirect('/contact')
        
    return render_template('contact.html')

@app.route('/courses')
def courses():
    # This would be replaced with actual course data later
    return "Courses page - Coming soon!"

@app.route('/resources')
def resources():
    # This would be replaced with actual resources data later
    return "Resources page - Coming soon!"

@app.route('/community')
def community():
    # This would be replaced with actual community features later
    return "Community page - Coming soon!"

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "Internal server error", 500

if __name__ == '__main__':
    app.run(debug=True)