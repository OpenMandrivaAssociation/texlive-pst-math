%global tl_name pst-math
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.67
Release:	%{tl_revision}.1
Summary:	Enhancement of PostScript math operators to use with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-math
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-math.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-math.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PostScript lacks a lot of basic operators such as tan, acos, asin, cosh,
sinh, tanh, acosh, asinh, atanh, exp (with e base). Also (oddly) cos and
sin use arguments in degrees. Pst-math provides all those operators in a
header file pst-math.pro with wrappers pst-math.sty and pst-math.tex. In
addition, sinc, gauss, gammaln and bessel are implemented (only
partially for the latter). The package is designed essentially to work
with pst-plot but can be used in whatever PS code (such as PSTricks
SpecialCoor "!", which is useful for placing labels). The package also
provides a routine SIMPSON for numerical integration and a solver of
linear equation systems.

