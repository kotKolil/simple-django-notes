# Simple Django Clipboard App

Simple Django Clipboard App - an open-source web application built with Django that allows users to create, view, and retrieve text notes via an API. Notes are categorized as either common (visible to everyone) or personal (visible only to the creator). The site includes a search function for finding specific notes. The frontend is built using HTML5 and CSS3, with page content generated using Jinja2 templates.

## API

The web app's API is built using Django Rest Framework. This framework provides API classes and authentication permissions. I've created endpoints on top of this foundation that allow users to view, create, and delete notes.

To send requests to this API, you need to include the necessary data in JSON format, including a "token" field for authentication.
