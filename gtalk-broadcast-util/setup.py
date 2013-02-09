from setuptools import setup

setup(
    name = "GTalk-Broadcast-Util",
    version = "0.0.1",
    author = "Andrey Khobnya",
    author_email = "andrey@khobnya.me",
    description = "Script for broadcasting in GTalk",
    license = "MIT",
    keywords = "Gtalk, XMPP, broadcast",
    py_modules=['gtb'],
    install_requires=['xmpppy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat']
)