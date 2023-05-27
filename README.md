<!--
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503
-->

<a name="readme-top"></a>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RaylaKurosaki1503/Student_Information_System">
    <img src="assets/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Student Information System</h3>

  <p align="center">
    During the spring term in my freshman year of university, I took a Computer Science class where I learned how to code in Python. After passing that class, I decided that I like coding enough to pick it up as a hobby. One project that I wanted to do on the side was to create a program that would print out the grades I currently have. At the time, some of the professors don't update the grades in my university's SIS system so I took it upon myself to do it.
    <br />
    <a href="https://github.com/RaylaKurosaki1503/Student_Information_System/docs"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The main purpose of this project is to compute and print the grades of all the courses I have taken. Other features this project can do is compute the GPA, attempted credits, earned credits, GPA units, and points for each term and cumulatively.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This guide will assume you already have Python and PIP installed. If you do not have either of those, make sure you download both Python and PIP on your machine.

I have tested this project for Python versions 3.7 and onwards. If your Python version is v3.9 or later, then the project will work normally. If you have Python v3.7 or Python v3.8, then the project will throw a minor error. To fix this error, there are two solutions:
1. Install Python v3.9 or later (the more convient and easiest solution).
2. If you have an understanding of coding in Python, remove all type hints in every `.py` file (the more tedious and harder solution).

<!-- Requires to import pandas and openpyxl -->

### Installation

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```
pip install pandas, openpyxl
```

```
python src/Student-Information-System.py 'C:\path-to-Excel-file\filename.xlsx'
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Compute grades for each course and print the student's grades in a pretty, tabular format. 
- [x] Compute the student's cumulative GPA and GPA per term and and print them in a pretty, tabular format.
- [x] Compute the number of attempted credits, earned credits, GPA Units, and Points for each term and print them in a pretty, tabular format.
- [x] Compute the number of cumulative attempted credits, cumulative earned credits, cumulative GPA Units, and cumulative Points for each term and print them in a pretty, tabular format.
- [ ] Compute the grade the student needs to get on their final exam/project to earn a specific grade.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

See [`LICENSE.md`](LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Rayla Kurosaki - raylakurosaki1503@gmail.com

Project Link: [https://github.com/RaylaKurosaki1503/Student_Information_System][github-project-link]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[github-project-link]: https://github.com/RaylaKurosaki1503/Student_Information_System
