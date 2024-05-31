#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : granatier
Version  : 24.05.0
Release  : 66
URL      : https://download.kde.org/stable/release-service/24.05.0/src/granatier-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/granatier-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/granatier-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: granatier-bin = %{version}-%{release}
Requires: granatier-data = %{version}-%{release}
Requires: granatier-license = %{version}-%{release}
Requires: granatier-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the granatier package.
Group: Binaries
Requires: granatier-data = %{version}-%{release}
Requires: granatier-license = %{version}-%{release}

%description bin
bin components for the granatier package.


%package data
Summary: data components for the granatier package.
Group: Data

%description data
data components for the granatier package.


%package doc
Summary: doc components for the granatier package.
Group: Documentation

%description doc
doc components for the granatier package.


%package license
Summary: license components for the granatier package.
Group: Default

%description license
license components for the granatier package.


%package locales
Summary: locales components for the granatier package.
Group: Default

%description locales
locales components for the granatier package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n granatier-24.05.0
cd %{_builddir}/granatier-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716523012
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716523012
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/granatier
cp %{_builddir}/granatier-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/granatier/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/granatier-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/granatier/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/granatier-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/granatier/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/granatier-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/granatier/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/granatier-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/granatier/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/granatier-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/granatier/a4c60b3fefda228cd7439d3565df043192fef137 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang granatier
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/granatier
/usr/bin/granatier

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.granatier.desktop
/usr/share/config.kcfg/granatier.kcfg
/usr/share/granatier/arenas/clanbomber_Arena.desktop
/usr/share/granatier/arenas/clanbomber_Arena.xml
/usr/share/granatier/arenas/clanbomber_Big_Block.desktop
/usr/share/granatier/arenas/clanbomber_Big_Block.xml
/usr/share/granatier/arenas/clanbomber_Big_Standard.desktop
/usr/share/granatier/arenas/clanbomber_Big_Standard.xml
/usr/share/granatier/arenas/clanbomber_Blast_Matrix.desktop
/usr/share/granatier/arenas/clanbomber_Blast_Matrix.xml
/usr/share/granatier/arenas/clanbomber_Bloody_Ring.desktop
/usr/share/granatier/arenas/clanbomber_Bloody_Ring.xml
/usr/share/granatier/arenas/clanbomber_Boiling_Egg.desktop
/usr/share/granatier/arenas/clanbomber_Boiling_Egg.xml
/usr/share/granatier/arenas/clanbomber_Bomb_Attack.desktop
/usr/share/granatier/arenas/clanbomber_Bomb_Attack.xml
/usr/share/granatier/arenas/clanbomber_Broken_Heart.desktop
/usr/share/granatier/arenas/clanbomber_Broken_Heart.xml
/usr/share/granatier/arenas/clanbomber_Crammed.desktop
/usr/share/granatier/arenas/clanbomber_Crammed.xml
/usr/share/granatier/arenas/clanbomber_Death_Corridor.desktop
/usr/share/granatier/arenas/clanbomber_Death_Corridor.xml
/usr/share/granatier/arenas/clanbomber_Dilemma.desktop
/usr/share/granatier/arenas/clanbomber_Dilemma.xml
/usr/share/granatier/arenas/clanbomber_FearCircle.desktop
/usr/share/granatier/arenas/clanbomber_FearCircle.xml
/usr/share/granatier/arenas/clanbomber_FearCircle_Remix.desktop
/usr/share/granatier/arenas/clanbomber_FearCircle_Remix.xml
/usr/share/granatier/arenas/clanbomber_FireWheels.desktop
/usr/share/granatier/arenas/clanbomber_FireWheels.xml
/usr/share/granatier/arenas/clanbomber_Football.desktop
/usr/share/granatier/arenas/clanbomber_Football.xml
/usr/share/granatier/arenas/clanbomber_Four_Instance.desktop
/usr/share/granatier/arenas/clanbomber_Four_Instance.xml
/usr/share/granatier/arenas/clanbomber_Ghostbear.desktop
/usr/share/granatier/arenas/clanbomber_Ghostbear.xml
/usr/share/granatier/arenas/clanbomber_Hard_Work.desktop
/usr/share/granatier/arenas/clanbomber_Hard_Work.xml
/usr/share/granatier/arenas/clanbomber_Hole_Run.desktop
/usr/share/granatier/arenas/clanbomber_Hole_Run.xml
/usr/share/granatier/arenas/clanbomber_Huge_Standard.desktop
/usr/share/granatier/arenas/clanbomber_Huge_Standard.xml
/usr/share/granatier/arenas/clanbomber_Juicy_Lucy.desktop
/usr/share/granatier/arenas/clanbomber_Juicy_Lucy.xml
/usr/share/granatier/arenas/clanbomber_Kitchen.desktop
/usr/share/granatier/arenas/clanbomber_Kitchen.xml
/usr/share/granatier/arenas/clanbomber_Meeting.desktop
/usr/share/granatier/arenas/clanbomber_Meeting.xml
/usr/share/granatier/arenas/clanbomber_MungoBane.desktop
/usr/share/granatier/arenas/clanbomber_MungoBane.xml
/usr/share/granatier/arenas/clanbomber_Obstacle_Race.desktop
/usr/share/granatier/arenas/clanbomber_Obstacle_Race.xml
/usr/share/granatier/arenas/clanbomber_Overkill.desktop
/usr/share/granatier/arenas/clanbomber_Overkill.xml
/usr/share/granatier/arenas/clanbomber_Prison_Cells.desktop
/usr/share/granatier/arenas/clanbomber_Prison_Cells.xml
/usr/share/granatier/arenas/clanbomber_Redirection.desktop
/usr/share/granatier/arenas/clanbomber_Redirection.xml
/usr/share/granatier/arenas/clanbomber_Sixty_Nine.desktop
/usr/share/granatier/arenas/clanbomber_Sixty_Nine.xml
/usr/share/granatier/arenas/clanbomber_Small_Standard.desktop
/usr/share/granatier/arenas/clanbomber_Small_Standard.xml
/usr/share/granatier/arenas/clanbomber_Snake_Race.desktop
/usr/share/granatier/arenas/clanbomber_Snake_Race.xml
/usr/share/granatier/arenas/clanbomber_Tiny_Standard.desktop
/usr/share/granatier/arenas/clanbomber_Tiny_Standard.xml
/usr/share/granatier/arenas/clanbomber_Whole_Mess.desktop
/usr/share/granatier/arenas/clanbomber_Whole_Mess.xml
/usr/share/granatier/arenas/clover.desktop
/usr/share/granatier/arenas/clover.xml
/usr/share/granatier/arenas/crazy.desktop
/usr/share/granatier/arenas/crazy.xml
/usr/share/granatier/arenas/granatier.desktop
/usr/share/granatier/arenas/granatier.xml
/usr/share/granatier/arenas/labyrinth.desktop
/usr/share/granatier/arenas/labyrinth.xml
/usr/share/granatier/arenas/threeofthree.desktop
/usr/share/granatier/arenas/threeofthree.xml
/usr/share/granatier/players/player1.desktop
/usr/share/granatier/players/player1.svgz
/usr/share/granatier/players/player2.desktop
/usr/share/granatier/players/player2.svgz
/usr/share/granatier/players/player3.desktop
/usr/share/granatier/players/player3.svgz
/usr/share/granatier/players/player4.desktop
/usr/share/granatier/players/player4.svgz
/usr/share/granatier/players/player5.desktop
/usr/share/granatier/players/player5.svgz
/usr/share/granatier/sounds/break.wav
/usr/share/granatier/sounds/clear.wav
/usr/share/granatier/sounds/corpse_explode.wav
/usr/share/granatier/sounds/crunch.wav
/usr/share/granatier/sounds/deepfall.wav
/usr/share/granatier/sounds/die.wav
/usr/share/granatier/sounds/explode.wav
/usr/share/granatier/sounds/joint.wav
/usr/share/granatier/sounds/putbomb.wav
/usr/share/granatier/sounds/winlevel.wav
/usr/share/granatier/sounds/wow.wav
/usr/share/granatier/themes/clanbomber.desktop
/usr/share/granatier/themes/clanbomber.svgz
/usr/share/granatier/themes/clanbomber_preview.png
/usr/share/granatier/themes/granatier.desktop
/usr/share/granatier/themes/granatier.svgz
/usr/share/granatier/themes/granatier_preview.png
/usr/share/granatier/themes/waterbomb.desktop
/usr/share/granatier/themes/waterbomb.svgz
/usr/share/granatier/themes/waterbomb_preview.png
/usr/share/icons/hicolor/128x128/apps/granatier.png
/usr/share/icons/hicolor/16x16/apps/granatier.png
/usr/share/icons/hicolor/22x22/apps/granatier.png
/usr/share/icons/hicolor/32x32/apps/granatier.png
/usr/share/icons/hicolor/48x48/apps/granatier.png
/usr/share/icons/hicolor/64x64/apps/granatier.png
/usr/share/metainfo/org.kde.granatier.appdata.xml
/usr/share/qlogging-categories6/granatier.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/granatier/config_arena.png
/usr/share/doc/HTML/ca/granatier/config_arena_random_mode.png
/usr/share/doc/HTML/ca/granatier/config_general.png
/usr/share/doc/HTML/ca/granatier/config_player.png
/usr/share/doc/HTML/ca/granatier/config_theme.png
/usr/share/doc/HTML/ca/granatier/granatier.png
/usr/share/doc/HTML/ca/granatier/index.cache.bz2
/usr/share/doc/HTML/ca/granatier/index.docbook
/usr/share/doc/HTML/cs/granatier/index.cache.bz2
/usr/share/doc/HTML/cs/granatier/index.docbook
/usr/share/doc/HTML/de/granatier/index.cache.bz2
/usr/share/doc/HTML/de/granatier/index.docbook
/usr/share/doc/HTML/en/granatier/arena_arrow_right.png
/usr/share/doc/HTML/en/granatier/arena_block.png
/usr/share/doc/HTML/en/granatier/arena_bomb_mortar.png
/usr/share/doc/HTML/en/granatier/arena_ground.png
/usr/share/doc/HTML/en/granatier/arena_ice.png
/usr/share/doc/HTML/en/granatier/arena_wall.png
/usr/share/doc/HTML/en/granatier/bonus_bad_hyperactive.png
/usr/share/doc/HTML/en/granatier/bonus_bad_mirror.png
/usr/share/doc/HTML/en/granatier/bonus_bad_restrain.png
/usr/share/doc/HTML/en/granatier/bonus_bad_scatty.png
/usr/share/doc/HTML/en/granatier/bonus_bad_slow.png
/usr/share/doc/HTML/en/granatier/bonus_bomb.png
/usr/share/doc/HTML/en/granatier/bonus_kick.png
/usr/share/doc/HTML/en/granatier/bonus_neutral_pandora.png
/usr/share/doc/HTML/en/granatier/bonus_neutral_resurrect.png
/usr/share/doc/HTML/en/granatier/bonus_power.png
/usr/share/doc/HTML/en/granatier/bonus_shield.png
/usr/share/doc/HTML/en/granatier/bonus_speed.png
/usr/share/doc/HTML/en/granatier/bonus_throw.png
/usr/share/doc/HTML/en/granatier/config_arena.png
/usr/share/doc/HTML/en/granatier/config_arena_random_mode.png
/usr/share/doc/HTML/en/granatier/config_general.png
/usr/share/doc/HTML/en/granatier/config_player.png
/usr/share/doc/HTML/en/granatier/config_theme.png
/usr/share/doc/HTML/en/granatier/granatier.png
/usr/share/doc/HTML/en/granatier/index.cache.bz2
/usr/share/doc/HTML/en/granatier/index.docbook
/usr/share/doc/HTML/es/granatier/index.cache.bz2
/usr/share/doc/HTML/es/granatier/index.docbook
/usr/share/doc/HTML/et/granatier/index.cache.bz2
/usr/share/doc/HTML/et/granatier/index.docbook
/usr/share/doc/HTML/fr/granatier/config_arena.png
/usr/share/doc/HTML/fr/granatier/config_general.png
/usr/share/doc/HTML/fr/granatier/config_player.png
/usr/share/doc/HTML/fr/granatier/config_theme.png
/usr/share/doc/HTML/fr/granatier/granatier.png
/usr/share/doc/HTML/fr/granatier/index.cache.bz2
/usr/share/doc/HTML/fr/granatier/index.docbook
/usr/share/doc/HTML/it/granatier/index.cache.bz2
/usr/share/doc/HTML/it/granatier/index.docbook
/usr/share/doc/HTML/nl/granatier/index.cache.bz2
/usr/share/doc/HTML/nl/granatier/index.docbook
/usr/share/doc/HTML/pt/granatier/index.cache.bz2
/usr/share/doc/HTML/pt/granatier/index.docbook
/usr/share/doc/HTML/pt_BR/granatier/index.cache.bz2
/usr/share/doc/HTML/pt_BR/granatier/index.docbook
/usr/share/doc/HTML/ru/granatier/index.cache.bz2
/usr/share/doc/HTML/ru/granatier/index.docbook
/usr/share/doc/HTML/sv/granatier/index.cache.bz2
/usr/share/doc/HTML/sv/granatier/index.docbook
/usr/share/doc/HTML/uk/granatier/config_arena.png
/usr/share/doc/HTML/uk/granatier/config_arena_random_mode.png
/usr/share/doc/HTML/uk/granatier/config_general.png
/usr/share/doc/HTML/uk/granatier/config_player.png
/usr/share/doc/HTML/uk/granatier/config_theme.png
/usr/share/doc/HTML/uk/granatier/granatier.png
/usr/share/doc/HTML/uk/granatier/index.cache.bz2
/usr/share/doc/HTML/uk/granatier/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/granatier/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/granatier/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/granatier/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/granatier/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/granatier/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/granatier/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f granatier.lang
%defattr(-,root,root,-)

