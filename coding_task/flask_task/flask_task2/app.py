from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    matches = []
    error = None
    test_string = ''
    regex_pattern = ''
    search_performed = False
    
    if request.method == 'POST':
        search_performed = True
        test_string = request.form.get('test_string', '')
        regex_pattern = request.form.get('regex_pattern', '')
        
        if test_string and regex_pattern:
            try:
                # Find all matches with details (positions, groups)
                pattern = re.compile(regex_pattern)
                match_objects = []
                for match in pattern.finditer(test_string):
                    match_data = {
                        'match': match.group(),
                        'start': match.start(),
                        'end': match.end(),
                        'groups': list(match.groups()) if match.groups() else []
                    }
                    match_objects.append(match_data)
                
                matches = match_objects
                    
            except re.error as e:
                error = f"Invalid regular expression: {str(e)}"
                matches = []
        else:
            error = "Please provide both test string and regular expression."
    
    return render_template('index.html', 
                         matches=matches, 
                         error=error,
                         test_string=test_string,
                         regex_pattern=regex_pattern,
                         search_performed=search_performed)

if __name__ == '__main__':
    app.run(debug=True)

