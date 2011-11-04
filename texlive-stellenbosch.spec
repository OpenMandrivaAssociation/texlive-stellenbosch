# revision 23900
# category Package
# catalog-ctan /macros/latex/contrib/stellenbosch
# catalog-date 2011-09-10 10:43:29 +0200
# catalog-license lppl
# catalog-version 4.2
Name:		texlive-stellenbosch
Version:	4.2
Release:	1
Summary:	Stellenbosch thesis bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stellenbosch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stellenbosch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stellenbosch.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stellenbosch.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/stellenbosch/usmeg-a.bst
%{_texmfdistdir}/bibtex/bst/stellenbosch/usmeg-n.bst
%{_texmfdistdir}/bibtex/bst/stellenbosch/ussagus.bst
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo-BW-top.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo-BW-top.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo-BW.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo-BW.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo-top.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo-top.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USEngLogo.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-BW.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-BW.jpg
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-WM.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-WM.jpg
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-stack.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-stack.jpg
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-top.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest-top.jpg
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/UScrest.jpg
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-BW.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-BW.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-gold.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-gold.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-grey.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-grey.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-maroon.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USleaf-maroon.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW-left.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW-left.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW-stack.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW-stack.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW-top.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW-top.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-BW.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-left.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-left.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-stack.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-stack.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-top.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo-top.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo.eps
%{_texmfdistdir}/tex/latex/stellenbosch/logos/USlogo.pdf
%{_texmfdistdir}/tex/latex/stellenbosch/usbib.afr
%{_texmfdistdir}/tex/latex/stellenbosch/usbib.eng
%{_texmfdistdir}/tex/latex/stellenbosch/usbib.sty
%{_texmfdistdir}/tex/latex/stellenbosch/usnomencl.sty
%{_texmfdistdir}/tex/latex/stellenbosch/ussummary.sty
%{_texmfdistdir}/tex/latex/stellenbosch/usthesis.afr
%{_texmfdistdir}/tex/latex/stellenbosch/usthesis.cls
%{_texmfdistdir}/tex/latex/stellenbosch/usthesis.eng
%{_texmfdistdir}/tex/latex/stellenbosch/usthesis.sty
%{_texmfdistdir}/tex/latex/stellenbosch/ustitle.sty
%doc %{_texmfdistdir}/doc/latex/stellenbosch/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/stellenbosch/README
%doc %{_texmfdistdir}/doc/latex/stellenbosch/USbib-1.0.pdf
%doc %{_texmfdistdir}/doc/latex/stellenbosch/USlogos-doc-4.0.pdf
%doc %{_texmfdistdir}/doc/latex/stellenbosch/USnomencl-1.1.pdf
%doc %{_texmfdistdir}/doc/latex/stellenbosch/USsummary-1.0a.pdf
%doc %{_texmfdistdir}/doc/latex/stellenbosch/USthesis-4.2.pdf
%doc %{_texmfdistdir}/doc/latex/stellenbosch/UStitle-1.0.pdf
%doc %{_texmfdistdir}/doc/latex/stellenbosch/templates/masters-sample.zip
%doc %{_texmfdistdir}/doc/latex/stellenbosch/templates/report-sample.zip
#- source
%doc %{_texmfdistdir}/source/latex/stellenbosch/USbib-1.0-scr.zip
%doc %{_texmfdistdir}/source/latex/stellenbosch/USlogos-4.0-src.zip
%doc %{_texmfdistdir}/source/latex/stellenbosch/USnomencl-1.1-src.zip
%doc %{_texmfdistdir}/source/latex/stellenbosch/USsummary-1.0a-src.zip
%doc %{_texmfdistdir}/source/latex/stellenbosch/USthesis-4.2-src.zip
%doc %{_texmfdistdir}/source/latex/stellenbosch/UStitle-1.0-src.zip
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
