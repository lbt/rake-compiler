#
# spec file for package rubygem-rake-compiler (Version 0.6.0)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           rubygem-rake-compiler
Version:        0.7.6
Release:        0
%define mod_name rake-compiler
#
Group:          Development/Languages/Ruby
License:        MIT
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
BuildRequires:  rubygem-rake >= 0.8.3
Requires:       rubygem-rake >= 0.8.3
BuildRequires:  rubygem-rake < 0.9
Requires:       rubygem-rake < 0.9
#
Url:            http://github.com/luislavena/rake-compiler
Source:         %{mod_name}-%{version}.gem
#
Summary:        Rake-based Ruby C Extension task generator
%description
Provide a standard and simplified way to build and package
Ruby C extensions using Rake as glue.

%prep
%build
%install
%gem_install %{S:0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/rake-compiler
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%changelog
