# revision 20176
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-math
# catalog-date 2010-10-02 23:46:37 +0200
# catalog-license lppl
# catalog-version 0.61
Name:		texlive-pst-math
Version:	0.61
Release:	1
Summary:	Enhancement of PostScript math operators to use with pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-math.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-math.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-math.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
PostScript lacks a lot of basic operators such as tan, acos,
asin, cosh, sinh, tanh, acosh, asinh, atanh, exp (with e base).
Also (oddly) cos and sin use arguments in degrees. Pst-math
provides all those operators in a header file pst-math.pro with
wrappers pst-math.sty and pst-math.tex. In addition, sinc,
gauss, gammaln and bessel are implemented (only partially for
the latter). pst-math is designed essentially to work with pst-
plot but can be used in whatever PS code (such as pstricks
SpecialCoor "!", which is useful for placing labels). The
package also provides a routine SIMPSON for numerical
integration and a solver of linear equation systems.

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
%{_texmfdistdir}/dvips/pst-math/pst-math.pro
%{_texmfdistdir}/tex/generic/pst-math/pst-math.tex
%{_texmfdistdir}/tex/latex/pst-math/pst-math.sty
%doc %{_texmfdistdir}/doc/generic/pst-math/Changes
%doc %{_texmfdistdir}/doc/generic/pst-math/README
%doc %{_texmfdistdir}/doc/generic/pst-math/pst-math-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-math/pst-math-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-math/pst-math-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-math/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
