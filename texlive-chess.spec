%global tl_name chess
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Fonts for typesetting chess boards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/chess/chess
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chess.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chess.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The original (and now somewhat dated) TeX chess font package. Potential
users should consider skak (for alternative fonts, and notation
support), texmate (for alternative notation support), or chessfss (for
flexible font choices).

