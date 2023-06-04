import re

html_pattern = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
print(re.sub(html_pattern, '', '<html><body>Hello, <b>world</b>!<br /></body></html>')) # returns 'Hello, world!'

string = '<div class="pv-text-details__left-panel"><div><h1 class="text-heading-xlarge inline t-24 v-align-middle break-words">Bas Smit</h1><!-- --><!-- --><!-- --><!-- --> </div><!-- --> <div class="text-body-medium break-words" data-generated-suggestion-target="urn:li:fsu_profileActionDelegate:2010681874">Having fun!</div><!-- --><!-- --><!-- --> </div>'

print(re.sub(html_pattern, '', string)) # returns 'Hello, world!'
