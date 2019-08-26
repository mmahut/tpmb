with import <nixpkgs> {};

let
  pythonModules = python37.withPackages(ps: [
    ps.pyserial
    ps.trezor
  ]);
in

stdenv.mkDerivation rec {
  name = "tpmb";
  buildInputs = [ uhubctl arduino pythonModules ];
}
