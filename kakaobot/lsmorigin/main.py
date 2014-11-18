#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

html = """
<!DOCTYPE html>
<html>
<head>
<title>Sung Min Zzang</title>
</head>
<body>
<h1>Hi! My name is Lim Sung Min!</br>I'm majoring in Computer Engineering!</h1>
<h2>Ummmm....And I really really hate English!! All Documentations are written by English!<br/></h2>
</body
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
