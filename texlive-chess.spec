Name:		texlive-chess
Version:	20582
Release:	2
Summary:	Fonts for typesetting chess boards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/chess/chess
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The original (and now somewhat dated) TeX chess font package.
Potential users should consider skak (for alternative fonts,
and notation support), texmate (for alternative notation
support), or chessfss (for flexible font choices).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/chess/README.mf
%{_texmfdistdir}/fonts/source/public/chess/chess10.mf
%{_texmfdistdir}/fonts/source/public/chess/chess20.mf
%{_texmfdistdir}/fonts/source/public/chess/chess30.mf
%{_texmfdistdir}/fonts/source/public/chess/chessbase.mf
%{_texmfdistdir}/fonts/source/public/chess/chessdiag.mf
%{_texmfdistdir}/fonts/source/public/chess/chessf10.mf
%{_texmfdistdir}/fonts/source/public/chess/chesspieces.mf
%{_texmfdistdir}/fonts/source/public/chess/empty.mf
%{_texmfdistdir}/fonts/tfm/public/chess/chess10.tfm
%{_texmfdistdir}/fonts/tfm/public/chess/chess20.tfm
%{_texmfdistdir}/fonts/tfm/public/chess/chess30.tfm
%{_texmfdistdir}/fonts/tfm/public/chess/chessf10.tfm
%{_texmfdistdir}/fonts/tfm/public/chess/chessfig10.tfm
%{_texmfdistdir}/tex/latex/chess/chess.sty
%doc %{_texmfdistdir}/doc/fonts/chess/board.epsf
%doc %{_texmfdistdir}/doc/fonts/chess/boards.ltx
%doc %{_texmfdistdir}/doc/fonts/chess/changes12
%doc %{_texmfdistdir}/doc/fonts/chess/chessdiag.Xmf
%doc %{_texmfdistdir}/doc/fonts/chess/copyright
%doc %{_texmfdistdir}/doc/fonts/chess/dutch-tt.ltx
%doc %{_texmfdistdir}/doc/fonts/chess/dutch-tt.tex
%doc %{_texmfdistdir}/doc/fonts/chess/installation
%doc %{_texmfdistdir}/doc/fonts/chess/kasparov.ltx
%doc %{_texmfdistdir}/doc/fonts/chess/makefile
%doc %{_texmfdistdir}/doc/fonts/chess/readme
%doc %{_texmfdistdir}/doc/fonts/chess/schaakmaatje.ltx
%doc %{_texmfdistdir}/doc/fonts/chess/symbols.ltx
%doc %{_texmfdistdir}/doc/fonts/chess/symbols.tex
%doc %{_texmfdistdir}/doc/fonts/chess/tal.ltx
%doc %{_texmfdistdir}/doc/fonts/chess/tal.tex
%doc %{_texmfdistdir}/doc/fonts/chess/tugboat.ltx
%doc %{_texmfdistdir}/doc/fonts/chess/tuggame.ltx

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
