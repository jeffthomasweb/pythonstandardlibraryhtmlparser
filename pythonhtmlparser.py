from html.parser import HTMLParser

#Use the standard library to parse HTML text

#Sample HTML
html_before_parse = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>NPR : National Public Radio</title>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <meta name="viewport" content="width=device-width">
    <link id="favicon" rel="shortcut icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAHlJREFUOBFjYBgFFIcA48cYpf/opvAv+YouxODXshZDbFONDSMLSJRv8V245KdYZTD7//8XcDFGRgkwe2O1NVzMv/UomA02AMQCaUQ2CCQG0ohsEEgMphHEBgEmCIWdRNeMTRXYBTBnw2iYQpjTYXx022Hio/RAhwAAjXEfJrIXnj4AAAAASUVORK5CYII=">
    <style>
        body {
    display: block;
    padding: 0px 20px;
    max-width: 550px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

.full-version-link {
    margin-left: 15px;
}

.slug-line {
    font-size: 1.1rem;
    margin-bottom: 15px;
}

.hr-line {
    position: relative;
    height: 4px;
}

.hr-line:after {
    background: linear-gradient(to right, #e60000 0%, #e60000 33.33%, #000000 33.33%, #000000 66.66%, #3366CC 66.66%);
    position: absolute;
    content: '';
    height: 4px;
    right: 0;
    left: 0;
    top: 0;
}

hr.gray {
    border: .5px solid gray;
}

.story-title {
    line-height: 2rem;
    font-size: 1.5rem;
    margin: 0;
}

.topic-heading {
    line-height: 2rem;
    font-size: 1.5rem;
}

.topic-container>ul {
    padding: 0;
    line-height: 1.4rem;
}

.topic-container li {
    display: block;
    padding-bottom: 15px;
}

.topic-container {
    margin-top: 20px;
}

.topic-date {
    margin: 20px 0;
    font-style: italic;
}

.paragraphs-container {
    line-height: 1.5rem;
}

.button:link,
.button:visited {
    background-color: white;
    color: black;
    border: 2px solid black;
    padding: 4px 8px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
}

.button:hover,
.button:active {
    background-color: black;
    color: white;
}

.lower-nav-container {
    margin-top: 40px;
}

.lower-nav-container li {
    margin-left: 0;
    display: inline;
    padding-right: 20px;
}

h6 {
  text-transform: uppercase;
}

    </style>
</head>


<body>
<header>
  <p>Text-Only Version <a class="full-version-link button" href="https://www.npr.org/">Go To Full Site</a></p>
</header>


<main>
  <p>
    
  </p>

  <div class="topic-container">
    <h1 class="topic-heading">NPR : National Public Radio</h1>
    <div class="hr-line"></div>
    <p class="topic-date">Wednesday, September 20, 2023</p>
    <ul>
      
        <li><a class="topic-title" href="/1200705608">Senate bucks Tuberville's blockade to begin approving military promotions</a></li>
      
        <li><a class="topic-title" href="/1200483937">Biden is unveiling the American Climate Corps, a program with echoes of the New Deal</a></li>
      
        <li><a class="topic-title" href="/1200674883">A 96-year-old federal judge was barred from hearing cases in a fight over her fitness</a></li>
      
        <li><a class="topic-title" href="/1200542589">This Republican senator wants an expanded child tax credit — with work requirements</a></li>
      
        <li><a class="topic-title" href="/1200130022">These 2020 census results break down people's race and ethnicity into details</a></li>
      
        <li><a class="topic-title" href="/1199192682">A federal agency wants to give safety tips to young adults. So it's dropping an album</a></li>
      
        <li><a class="topic-title" href="/1200197882">'Wellness' is a perfect novel for our age, its profound sadness tempered with humor</a></li>
      
        <li><a class="topic-title" href="/1200417169">Fed-up consumers are increasingly going after food companies for misleading claims</a></li>
      
        <li><a class="topic-title" href="/1200725583">Kraft is recalling some American cheese slices over potential choking hazard</a></li>
      
        <li><a class="topic-title" href="/1200592771">Having a hard time finding Clorox wipes? Blame it on a cyberattack</a></li>
      
        <li><a class="topic-title" href="/1200719816">U.S. will expand Temporary Protected Status to hundreds of thousands of Venezuelans</a></li>
      
        <li><a class="topic-title" href="/1200009089">You've likely seen this ranch on-screen — burned by wildfire, it awaits its next act</a></li>
      
        <li><a class="topic-title" href="/1200386054">As the U.S. considers more aid to Ukraine, Zelenskyy says 'we have the same values'</a></li>
      
        <li><a class="topic-title" href="/1200327332">The Federal Reserve holds interest rates steady but hints at more action this year</a></li>
      
        <li><a class="topic-title" href="/1200712487">Biden is creating a new White House office focused on gun violence prevention</a></li>
      
        <li><a class="topic-title" href="/1200626587">UAW strike latest: GM sends 2,000 workers home in Kansas</a></li>
      
        <li><a class="topic-title" href="/1200430655">AG Garland defends DOJ's Hunter Biden investigation at House Judiciary hearing</a></li>
      
        <li><a class="topic-title" href="/1200569975">What to know about the tensions between Canada and India over the killing of a Sikh</a></li>
      
        <li><a class="topic-title" href="/1199011221">Planting a meadow and growing a community</a></li>
      
        <li><a class="topic-title" href="/1200647985">There have been attempts to censor more than 1,900 library book titles so far in 2023</a></li>
      
    </ul>
  </div>
</main>


<div class="hr-line"></div>
<nav>
<p>Topics</p>
<ul>
    <li><a href="/1001">News</a></li>
    <li><a href="/1008">Culture</a></li>
    <li><a href="/1039">Music</a></li>
</ul>
</nav>


<footer>
  <nav class="lower-nav-container">
    <li><a href="/614470770">Contact Us</a></li>
    <li><a href="/179876898">Terms of Use</a></li>
    <li><a href="/179881519">Permissions</a></li>
    <li><a href="/179878450">Privacy Policy</a></li>
  </nav>

  <p>&copy NPR</p>
</footer>

</body>
</html>
"""


list_of_html_text = []

#HTMLParser from the standard library has a method called handle_data that I implemented to pass text data into list_of_html_text
class MyHtmlParser(HTMLParser):
    def handle_data(self, data):
        list_of_html_text.append(data)

parser = MyHtmlParser()
parser.feed(html_before_parse)

#There are a number of "\n" characters and style css in the text. Create a list to put the cleaned text into.
list_cleaned_of_newlines = []

for x in list_of_html_text:
    if (x.find("\\") <0 and x.find("{") <0 and x.find("\n") <0):
        list_cleaned_of_newlines.append(x)

for i in list_cleaned_of_newlines:
    print(i)

"""
Sample output below:

NPR : National Public Radio
Text-Only Version 
Go To Full Site
NPR : National Public Radio
Wednesday, September 20, 2023
Senate bucks Tuberville's blockade to begin approving military promotions
Biden is unveiling the American Climate Corps, a program with echoes of the New Deal
A 96-year-old federal judge was barred from hearing cases in a fight over her fitness
This Republican senator wants an expanded child tax credit — with work requirements
These 2020 census results break down people's race and ethnicity into details
A federal agency wants to give safety tips to young adults. So it's dropping an album
'Wellness' is a perfect novel for our age, its profound sadness tempered with humor
Fed-up consumers are increasingly going after food companies for misleading claims
Kraft is recalling some American cheese slices over potential choking hazard
Having a hard time finding Clorox wipes? Blame it on a cyberattack
U.S. will expand Temporary Protected Status to hundreds of thousands of Venezuelans
You've likely seen this ranch on-screen — burned by wildfire, it awaits its next act
As the U.S. considers more aid to Ukraine, Zelenskyy says 'we have the same values'
The Federal Reserve holds interest rates steady but hints at more action this year
Biden is creating a new White House office focused on gun violence prevention
UAW strike latest: GM sends 2,000 workers home in Kansas
AG Garland defends DOJ's Hunter Biden investigation at House Judiciary hearing
What to know about the tensions between Canada and India over the killing of a Sikh
Planting a meadow and growing a community
There have been attempts to censor more than 1,900 library book titles so far in 2023
Topics
News
Culture
Music
Contact Us
Terms of Use
Permissions
Privacy Policy
© NPR
"""
