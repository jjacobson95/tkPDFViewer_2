import setuptools

with open("README.md","r") as f:
    long_description = f.read()

setuptools.setup(
  name = 'tkPDFViewer_2',
  packages = ['tkPDFViewer_2'],
  version = '0.1',
  license='MIT',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  description = 'The tkPDFViewer is python library, which allows you to embed the PDF file in your tkinter GUI',
  author = 'Jeremy Jacobson',
  author_email = 'jeremy.jacobson3402@gmail.com',
  url = 'https://github.com/jjacobson95/',
  download_url = 'https://github.com/jjacobson95/tkPDFViewer_2/archive/0.1.zip',
  keywords = ['PdfViewer', 'tkinter', 'pdf'],
  install_requires=[
          'PyMuPDF',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
