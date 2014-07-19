Summary:	Khronos OpenGL registry
Summary(pl.UTF-8):	Rejest Khronos OpenGL
Name:		khronos-opengl-registry
Version:	20140715
Release:	1
License:	SGI Free Software License B
Group:		Development/Libraries
# svn co https://cvs.khronos.org/svn/repos/ogl/trunk/doc/registry/public/api/
# tar cJf ogl-api.tar.xz api
Source0:	ogl-api.tar.xz
# Source0-md5:	ff1ca6e96863257d98838f8918609ba8
URL:		http://www.opengl.org/registry/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Khronos Group OpenGL registry XML defining the APIs and reserved
enumerant ranges for OpenGL, GLX, WGL and EGL.

%description -l pl.UTF-8
Pliki XML rejestru OpenGL Grupy Khronos definiujące API oraz
zarezerwowane przedziały liczbowe dla OpenGL, GLX, WGL oraz EGL.

%prep
%setup -q -c

%{__sed} -i -e '1s,/usr/bin/env python,/usr/bin/python,' api/genheaders.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/opengl/api,%{_npkgconfigdir}}

cp -p api/{genheaders.py,reg.py,registry.rnc,*.xml} $RPM_BUILD_ROOT%{_datadir}/opengl/api

cat >$RPM_BUILD_ROOT%{_npkgconfigdir}/khronos-opengl-registry.pc <<EOF
prefix=%{_prefix}
datadir=%{_datadir}
specdir=%{_datadir}/opengl/api
Name: %{name}
Description: Khronos OpenGL registry
Version: %{version}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc api/readme.pdf
%dir %{_datadir}/opengl
%dir %{_datadir}/opengl/api
%attr(755,root,root) %{_datadir}/opengl/api/genheaders.py
%attr(755,root,root) %{_datadir}/opengl/api/reg.py
%{_datadir}/opengl/api/registry.rnc
%{_datadir}/opengl/api/*.xml
%{_npkgconfigdir}/khronos-opengl-registry.pc
