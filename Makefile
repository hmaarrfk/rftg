PACKAGE_NAME=rftg

all:
	rpmdev-setuptree
	spectool -g -R $(PACKAGE_NAME).spec
	cp $(PACKAGE_NAME).png   ~/rpmbuild/SOURCES/
	cp $(PACKAGE_NAME).desktop   ~/rpmbuild/SOURCES/
	cp $(PACKAGE_NAME).appdata.xml ~/rpmbuild/SOURCES/
	rpmbuild -bs $(PACKAGE_NAME).spec


.PHONY: all
