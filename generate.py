template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <title>{{name}}</title>
</head>
<body>
    <div class="background"></div>
    <main>
        <image src="https://assets.hackclub.com/flag-orpheus-top.svg" class="orpheus-flag"></image>
        <div class="front">
            <h1 class="title">
                {{name}}
            </h1>
            <h2 class="caption">
                {{caption}}
            </h2>
            <h3 class="information">
                {{information}}
            </h3>
            <div class="signup">
                <input id="signup-input" type="text" class="email" placeholder="Email Address">
                <button id="signup-button" onclick="signup()">Sign Up</button>
            </div>
        </div>
    </main>
    <script>
        
        function signup() {
            email = document.getElementById('signup-input').value
            email = encodeURIComponent(email)
            window.location.href = '{{form_link}}' + email
        }
    </script>
</body>
</html>
"""

event_name = input ("Enter the event name: ") or "Event Name"
event_caption = input ("Enter the event caption: ") or "Event Caption"
event_information = input ("Enter the event information: ") or "Event Information"
form_link = input ("Enter the form link: ") or "https://airtable.com/apptaIuqOvOYiV4Y0/pagVhhNdnmGwzmiAB/form"
form_prefill_field_name = input ("Enter the prefill field name: ") or "Email"

def encode(s):
    replacementMap = {
        " ": "+",
        "!": "%21",
        '"': "%22",
        "#": "%23",
        "$": "%24",
        "%": "%25",
        "&": "%26",
        "'": "%27",
        "(": "%28",
        ")": "%29",
        "*": "%2A",
        "+": "%2B",
        ",": "%2C",
        "-": "%2D",
        ".": "%\2E",
        "/": "%\2F",
        ":": "%3A",
        ";": "%3B",
        "<": "%3C",
        "=": "%3D",
        ">": "%\3E",
        "?": "%\3F",
        "@": "%40",
        "[": "%5B",
        "\\": "%5C",
        "]": "%5D",
        "^": "%\5E",
        "_": "%\5F",
        "`": "%60",
        "{": "%7B",
        "|": "%7C",
        "}": "%7D",
        "~": "%\7E",
    }
    for key in replacementMap:
        s = s.replace(key, replacementMap[key])

    return s
    
template = template.replace("{{name}}", event_name)
template = template.replace("{{caption}}", event_caption)
template = template.replace("{{information}}", event_information)
template = template.replace("{{form_link}}", form_link+"?prefill_"+encode(form_prefill_field_name)+"=")

import datetime
now = datetime.datetime.now()
filename = "event_"+now.strftime("%Y-%m-%d_%H-%M-%S")+".html"

with open(filename, "w") as f:
    f.write(template)

print("File generated: ", filename)