
all:
	rpmdev-setuptree
	spectool -g *.spec
	cp *.spec ~/rpmbuild/SPECS/
	cp *.tar.* ~/rpmbuild/SOURCES/
	cp *.png   ~/rpmbuild/SOURCES/
	cp *.desktop   ~/rpmbuild/SOURCES/
	cp *.appdata.xml ~/rpmbuild/SOURCES/
	rpmbuild -bs ~/rpmbuild/SPECS/rftg.spec


.PHONY: all
