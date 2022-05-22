import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Salman Shaikh
##### *Resume* 
''')

image = Image.open('Salman_Circle.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- 6+ years of Industry Experience with 3.5 years of Experience as a Data Scientist using Machine Learning Algorithms and Computer Vision.
- Proficient in predictive modeling, data processing, and data mining algorithms, as well as scripting languages, including Python.
- Working Experience & Extensive knowledge in Python with libraries such as Sklearn, TensorFlow, PyTorch, Pytesseract, DocTR, LayoutParser, FastAPI, Streamlit, Numpy, Pandas, Matplotlib, Seaborn and data visualization tool such as Tableau and PowerBi.
- Strong verbal and written communication skills.
''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #15A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/salman-shaikh0706/" target="_blank">Salman Shaikh</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('''
## Education
''')

txt('**Bachelor of Technology** (Computer Science), *Jawaharlal Nehru Technological University*, Hyderabad',
    '2010-2014')

txt('**Senior Secondary**, *DAV Public School*, Ranchi',
    '2008-2010')

txt('**Higher Secondary**, *DAV Public School*, Ranchi',
    '2008')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist**, ***Capgemini***,Client: DBS Bank, Bangalore, India',
    '08/2021 - Current')
st.markdown('''
- Worked on Intelligent classification of emails using BERT model and pretrained an industry first Financial Markets NLP deep learning model - Treasury & Markets BERT (TMBERT)
- Worked on Automatic Speech Recognition (ASR) using Nvidia's Nemo model.
- Worked on to extract table from a image document using different Deep Learning Based Document Image Analysis toolkit such as LayoutParser, DocTR, Tensorflow.
- Automated multiple manual task such as using pyteserract to read test out of image files and extract the required informations out off it.
- Created a Tableau dashboard to display the Data Science findings in real-time.
- Drive the interaction and partnership between the managers to ensure active cooperation in identifying as well as defining analytical needs, and generating the pull-through of insights with the business.
- Utilized analytical and technical expertise to provide insights and proposals to support business improvements.
''')

txt('**Data Scientist**, ***Wipro Limited***,Client: NBN Telecom, Bangalore, India',
    '02/2021 - 08/2021')
st.markdown('''
- Implemented discretization and binning, data wrangling: cleaning, transforming, merging and reshaping data frames using Python-Pandas.
- Designed data visualization to present current impact and growth using Python’s module such as Matplotlib, Seaborn and Pyplot.
- Automated the report release process, bring the total time for code releases from 8 hours to 1 hour.
- Discusses technical and design issues with other developers, managers, users or customers whenever necessary to achieve best solution.
''')

txt('**Data Analyst**, ***CGI Inc***,Client: Starr Insurance, Bangalore, India',
    '11/2018 - 02/2021')
st.markdown('''
- Involvement of Incident Management and Problem.
- Management to handle the process. Automation of task using Script.
- Modify/create UNIX scripts for scheduling various data cleansing scripts and loading process.
''')

txt('**Associate Software Engineer**, ***CGI Inc***,Client: Bell Canada, Bangalore, India',
    '05/2016 - 10/2018')
st.markdown('''
- Involvement of Incident Management and Problem
- Designed data visualization to present current impact and growth using Python’s module such as Matplotlib, Seaborn and Pyplot.
- Automated the report release process, bring the total time for code releases from 8 hours to 1 hour.
''')

st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Shell Scripting`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`,`OpenCV`,`Keras`,`NLTK`')
txt3('Deep Learning', '`TensorFlow`,`PyTorch`,`LayoutParser`,`DocTR`')
txt3('Web development', '`Django`,`FastAPI`,`Streamlit`,`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`Streamlit`, `Github`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/salman-shaikh0706/')
txt2('GitHub', 'https://github.com/shaikhsalman0706')

