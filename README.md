
![logo](https://raw.githubusercontent.com/therexone/pyDoodle2Web/master/pyDoodle2Web.png)


A handy tool written in Python that converts hand drawn doodles into Bootstrap html website template.

### Installation
``pip install``

### Run the django server
``python manage.py runserver``

#### Uploading a doodle
The upload page has a custom [LiterallyCanvas](http://literallycanvas.com/) canvas where the wireframes can be drawn and downloaded.

> Check out the [example doodle](https://github.com/therexone/pyDoodle2Web/blob/master/referenceDoodle.png)

#### Naming Convention
Currently these basic components of Bootstrap 4 are supported:

- [navbar](https://getbootstrap.com/docs/4.4/components/navbar/)
- [container](https://getbootstrap.com/docs/4.4/layout/overview/#containers)
- [row](https://getbootstrap.com/docs/4.4/layout/grid/#row-columns)
- [column(col)](https://getbootstrap.com/docs/4.4/layout/grid/#auto-layout-columns)
- [image](https://getbootstrap.com/docs/4.4/content/images/)
- [card](https://getbootstrap.com/docs/4.4/components/card/)
- [carousel](https://getbootstrap.com/docs/4.4/components/carousel/)
- Text

> Parent like components(``container, row, col``) require a closing tag with ``-end``
>> ``container`` requires a ``container-end``

>> ``row`` requires a ``row-end``

>> ``column`` requires a ``column-end``


