#!/usr/bin/python2
from rjsmin import jsmin
from rcssmin import cssmin


def minify_css_proc(src_text):
    return cssmin(src_text, keep_bang_comments=True)


def minify_js_proc(src_text):
    return jsmin(src_text)


def do_process_files(minify_proc, source_paths, header, dest_path, min_path):
    print("Combining to %s and %s" % (dest_path, min_path))
    f = open(dest_path, 'w')
    mf = open(min_path, 'w')
    try:
        mf.write(header)
        for srcFile in source_paths:
            print(srcFile)
            with open(srcFile) as inputFile:
                src_text = inputFile.read()
                min_text = minify_proc(src_text)
                print(min_path, min_text)
            f.write(src_text)
            mf.write(min_text)
    finally:
        f.close()
        if mf and not mf.closed:
            mf.close()


def doJSMin(source_paths, header, dest_path, min_path):
    return do_process_files(minify_js_proc, source_paths, header, dest_path, min_path)


def doCSSMin(source_paths, dest_path, min_path):
    return do_process_files(minify_css_proc, source_paths, '', dest_path, min_path)

js_dest_path = "static/js/combine.js"
js_min_path = "static/js/combine.min.js"
js_header_path = "jslicenses.js"

js_sources = [
    "static/js/FlickrAPI.js",
    "static/js/Flickr.Gallery.js",
    "static/js/custom.js"
]

css_dest_path = "static/css/combine.css"
css_min_path = "static/css/combine.min.css"

css_sources = [
    "static/css/gallery.css",
    "static/css/custom_gallery.css",
]


if __name__ == '__main__':
    jsHeader = ''
    doJSMin(js_sources, jsHeader, js_dest_path, js_min_path)
    doCSSMin(css_sources, css_dest_path, css_min_path)
