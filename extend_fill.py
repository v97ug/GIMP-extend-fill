#!/usr/bin/python
# coding: UTF-8

from gimpfu import *

def extend_and_fill(image, drawable):
    pdb.gimp_selection_grow(image, 1)
    pdb.gimp_edit_fill(drawable, 0)


register(
        proc_name = "python_fu_extend_fill",
        blurb = "選択範囲を１pixel拡大し、その中を描画色で塗りつぶす。",
        help = "選択範囲を１pixel拡大し、その中を描画色で塗りつぶす。",
        author = "v97ug",
        copyright = "v97ug",
        date = "2017",
        label = "<Image>/Edit/extend1_and_fill",
        imagetypes = "*",
        params = [],
        results = [],
        function = extend_and_fill)

main()
