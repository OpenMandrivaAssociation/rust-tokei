# Generated by rust2rpm 13
%bcond_without check

%global crate tokei

Name:           rust-%{crate}
Version:        10.1.1
Release:        2%{?dist}
Summary:        Utility that allows you to count code, quickly

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/tokei
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Utility that allows you to count code, quickly.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENCE-MIT LICENCE-APACHE
%{_bindir}/tokei
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENCE-MIT LICENCE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages
which use "all" feature of "%{crate}" crate.

%files       -n %{name}+all-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cbor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cbor-devel %{_description}

This package contains library source intended for building other packages
which use "cbor" feature of "%{crate}" crate.

%files       -n %{name}+cbor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+hex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hex-devel %{_description}

This package contains library source intended for building other packages
which use "hex" feature of "%{crate}" crate.

%files       -n %{name}+hex-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages
which use "json" feature of "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_cbor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_cbor-devel %{_description}

This package contains library source intended for building other packages
which use "serde_cbor" feature of "%{crate}" crate.

%files       -n %{name}+serde_cbor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_yaml-devel %{_description}

This package contains library source intended for building other packages
which use "serde_yaml" feature of "%{crate}" crate.

%files       -n %{name}+serde_yaml-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages
which use "yaml" feature of "%{crate}" crate.

%files       -n %{name}+yaml-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 10.1.1-1
- Update to 10.1.1

* Wed Dec 25 11:00:37 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.1.0-2
- Update git2 to 0.11

* Tue Nov 19 09:33:39 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.1.0-1
- Update to 10.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 11:20:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.0.1-1
- Update to 10.0.1

* Wed Jun 19 12:33:03 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.0.0-1
- Update to 10.0.0

* Fri Jun 07 2019 Josh Stone <jistone@redhat.com> - 9.1.1-2
- Bump git2 to 0.9

* Sat Mar 30 14:59:32 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 9.1.1-1
- Update to 9.1.1

* Thu Mar 21 09:59:47 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 9.1.0-1
- Update to 9.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Josh Stone <jistone@redhat.com> - 9.0.0-1
- Update to 9.0.0

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.0.1-2
- Adapt to new packaging

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.0.1-1
- Update to 8.0.1

* Wed Jul 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.3-4
- Bump handlebars to 1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.3-2
- Update to new macro

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.3-1
- Update to 7.0.3

* Wed Feb 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.1-6
- Rebuild for passing %%__cargo_common_opts bug

* Tue Feb 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.1-5
- Bump rayon to 1

* Mon Feb 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.1-4
- Bump ignore to 0.4

* Sat Feb 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.1-3
- Bump handlebars to 0.31

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.1-1
- Update to 7.0.1

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.0-3
- Rebuild for env_logger 0.5.2

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.0-2
- Rebuild for env_logger 0.5.1

* Wed Jan 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-8
- Rebuild for rust-packaging v5

* Tue Jan 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-7
- Bump serde_cbor to 0.8

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-6
- Bump lazy_static to 1

* Tue Nov 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-5
- Rebuild for clap 2.28.0

* Sat Nov 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-4
- Rebuild for rust-hex 0.3

* Wed Nov 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-3
- Rebuild for dependency change

* Wed Nov 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-2
- Enable all feauteres

* Tue Nov 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-1
- Initial package
