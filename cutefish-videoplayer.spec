%define _empty_manifest_terminate_build 0
%define oname videoplayer

Name:           cutefish-videoplayer
Version:        0.5
Release:        3
Summary:        Video Player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/cutefishos/videoplayer
Source:         https://github.com/cutefishos/videoplayer/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(Breeze)
BuildRequires:  cmake(FishUI)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
#uildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(mpv)

Requires:       fishui
Requires:       mpv

%description
An open source video player built with Qt/QML and libmpv. Based on haruna.
Features
 - these are just some features that set Haruna apart from others players
 - play online videos, through youtube-dl
 - toggle playlist with mouse-over, playlist overlays the video
 - auto skip chapter containing certain words
 - configurable shortcuts and mouse buttons
 - quick jump to next chapter by middle click on progress bar

%prep
%autosetup -n %{oname}-%{version} -p1
sed -i "s/^\(Exec=\).*/\1%{name}/" %{name}.desktop
sed -i 's/^\(Icon=\).*/\1multimedia-video-player/' %{name}.desktop

%build
mkdir build
pushd build
# FIXME: you should use the %%cmake macros
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build
popd

%install
%make_install -C build
install -Dm 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
