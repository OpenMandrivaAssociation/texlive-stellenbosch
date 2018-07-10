Name:		texlive-stellenbosch
Version:	11a
Release:	2
Summary:	Stellenbosch thesis bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stellenbosch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stellenbosch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stellenbosch.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stellenbosch.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The usthesis class/style files are provided to typeset reports,
theses and dissertations that conform to the requirements of
the Engineering Faculty of the University of Stellenbosch. The
class file usthesis.cls is based on the standard LaTeX book
class, while usthesis.sty is a style file to be loaded on top
of the very powerful memoir class. Both options give identical
output, but the benefit of the using memoir is that it has many
additional command and environments for formatting and
processing of a document. Usthesis is primarily concerned with
the formatting of the front matter such as the title page,
abstract, etc. and a decent page layout on A4 paper. It also
works together with the babel package to provide language
options to typeset documents in Afrikaans or in English.
Additional packages are provided for bibliographic matter, note
title pages, lists of symbols, as well as various graphic files
for logos.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/stellenbosch
%{_texmfdistdir}/tex/latex/stellenbosch
%doc %{_texmfdistdir}/doc/latex/stellenbosch
#- source
%doc %{_texmfdistdir}/source/latex/stellenbosch

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
