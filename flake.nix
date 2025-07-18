{
  description = "mr-poopybutthole Python dev shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";

  outputs = { self, nixpkgs, ... }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [ 
        python310
        pipenv
        python310Packages.cython
        gcc
        libffi
        openssl
        zlib
        bzip2
        xz
        stdenv.cc.cc.lib
      ];

      shellHook = ''
        export PIPENV_PYTHON="${pkgs.python310}/bin/python"
        if [ ! -d .venv ]; then
          echo "📦 No .venv found — running pipenv install..."
          pipenv install || echo "⚠️ pipenv install failed"
        fi
      '';
    };
  };
}
