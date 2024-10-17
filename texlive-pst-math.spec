Name:		texlive-pst-math
Version:	67535
Release:	1
Summary:	Enhancement of PostScript math operators to use with pstricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-math
%{_texmfdistdir}/tex/generic/pst-math
%{_texmfdistdir}/tex/latex/pst-math
%doc %{_texmfdistdir}/doc/generic/pst-math

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
