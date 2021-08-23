with import <nixpkgs> {} ;

mkShell {
  nativeBuildInputs = [ qt5.qttools.dev ];
  propagatedBuildInputs = with python3Packages; [
      matplotlib
      pandas
      bluepy
      pyqt5
    ];
  QT_QPA_PLATFORM_PLUGIN_PATH="${qt5.qtbase.bin}/lib/qt-${qt5.qtbase.version}/plugins";
}
