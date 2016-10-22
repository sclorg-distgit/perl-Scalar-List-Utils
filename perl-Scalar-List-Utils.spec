%{?scl:%scl_package perl-Scalar-List-Utils}

Name:           %{?scl_prefix}perl-Scalar-List-Utils
Epoch:          3
Version:        1.45
Release:        3%{?dist}
Summary:        A selection of general-utility scalar and list subroutines
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Scalar-List-Utils/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/Scalar-List-Utils-%{version}.tar.gz
# Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Runtime
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests only
BuildRequires:  %{?scl_prefix}perl(B::Deparse)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(Math::BigInt)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(threads)
BuildRequires:  %{?scl_prefix}perl(threads::shared)
BuildRequires:  %{?scl_prefix}perl(Tie::Handle)
BuildRequires:  %{?scl_prefix}perl(Tie::Scalar)
BuildRequires:  %{?scl_prefix}perl(Tie::StdScalar)
BuildRequires:  %{?scl_prefix}perl(vars)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)

%{?perl_default_filter}

%description
This package contains a selection of subroutines that people have expressed
would be nice to have in the perl core, but the usage would not really be
high enough to warrant the use of a keyword, and the size so small such
that being individual extensions would be wasteful.

%prep
%setup -q -n Scalar-List-Utils-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/List*
%{perl_vendorarch}/Scalar*
%{perl_vendorarch}/Sub*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 3:1.45-3
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3:1.45-2
- Increase epoch to favour standalone package

* Tue Mar 29 2016 Jan Pazdziora <jpazdziora@redhat.com> - 2:1.45-1
- 1.45 bump

* Fri Mar 18 2016 Jan Pazdziora <jpazdziora@redhat.com> - 2:1.44-1
- 1.44 bump

* Tue Feb 09 2016 Petr Šabata <contyk@redhat.com> - 2:1.43-1
- 1.43 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.42-2
- Perl 5.22 rebuild
- Increase Epoch to favour standalone package

* Tue May 26 2015 Petr Šabata <contyk@redhat.com> - 1:1.42-1
- 1.42 bump

* Mon Nov 24 2014 Petr Šabata <contyk@redhat.com> - 1:1.41-1
- 1.41 bump; various enhancements

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.38-5
- Increase Epoch to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Paul Howarth <paul@city-fan.org> - 1.38-1
- Update to 1.38
  - Skip pairmap()'s MULTICALL implementation 5.8.9/5.10.0 as it doesn't work
    (CPAN RT#87857)
  - Comment on the fact that package "0" is defined but false (CPAN RT#88201)
  - TODO test in t/readonly.t now passes since 5.19.3 (CPAN RT#88223)
  - Added any, all, none, notall list reduction functions (inspired by
    List::MoreUtils)
  - Added List::Util::product()
  - Added Scalar::Util::unweaken()
  - Avoid C99/C++-style comments in XS code
  - Fix dualvar tests for perl 5.6; fix skip() test counts in dualvar.t
  - Neater documentation examples of other functions that can be built using
    reduce
  - Implement reduce() and first() even in the absence of MULTICALL
  - Various documentation changes/updates
  - Correct uses of overload operators in unit tests (CPAN RT#91969)

* Fri Aug 16 2013 Iain Arnell <iarnell@gmail.com> 1.31-293
- update to latest upstream version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-292
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.27-291
- Specify all dependencies

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1.27-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.27-247
- Link minimal build-root packages against libperl.so explicitly

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-246
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 1.27-245
- update to latest upstream version

* Fri Aug 17 2012 Petr Pisar <ppisar@redhat.com> - 1.25-240
- Increase release to replace perl sub-package (bug #848961)

* Thu Aug 16 2012 Petr Pisar <ppisar@redhat.com> - 1.25-4
- Correct dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.25-2
- Perl 5.16 rebuild

* Sun Mar 25 2012 Iain Arnell <iarnell@gmail.com> 1.25-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.23-2
- Perl mass rebuild

* Mon Feb 21 2011 Iain Arnell <iarnell@gmail.com> 1.23-1
- Specfile autogenerated by cpanspec 1.79.
