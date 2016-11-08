import os

if __name__ == '__main__':

    name = raw_input("New Widget name: ")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # UI File
    tpl = 'QtSimpleWidget_UI.ui'
    target = 'Qt%sWidget_UI.ui' % (name)
    if not os.path.exists(target):
        print "Writing %s" % (target)
        with open(tpl, 'r') as fh:
            src = fh.read()
        src = src.replace("QtSimpleWidget", "Qt%sWidget" % (name))
        with open(target, 'w') as fh:
            fh.write(src)
    else:
        print "%s already exists" % (target)

    # Add compilation to SConstruct
    line = "env.UiClass('Qt{name}Widget_UI.py', 'Qt{name}Widget.ui')".format(name=name)
    target = 'SConstruct'
    with open(target, 'r') as fh:
        src = fh.read()
    if line not in src:
        print "Adding line to SContruct:"
        print " ", line
        with open(target, 'a') as fh:
            print >>fh, line
        print "Run scons to compile"

    # Python Widget file
    tpl = 'QtSimpleWidget.py'
    target = 'Qt%sWidget.py' % (name)
    if not os.path.exists(target):
        print "Writing %s" % (target)
        with open(tpl, 'r') as fh:
            src = fh.read()
        src = src.replace("Simple", name)
        with open(target, 'w') as fh:
            fh.write(src)
    else:
        print "%s already exists" % (target)

    # Python Presenter file
    tpl = 'QtSimpleQuestion.py'
    target = 'Qt%sQuestion.py' % (name)
    if not os.path.exists(target):
        print "Writing %s" % (target)
        with open(tpl, 'r') as fh:
            src = fh.read()
        src = src.replace("Simple", name)
        with open(target, 'w') as fh:
            fh.write(src)
    else:
        print "%s already exists" % (target)


    print "Done"