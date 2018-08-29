from conans import ConanFile, AutoToolsBuildEnvironment, tools

class Srtp(ConanFile):
    name = "srtp"
    version = "2.2.0"
    settings = "os", "compiler", "build_type", "arch"
    repo_url = "https://github.com/cisco/libsrtp"

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.repo_url, self.version))

    def build(self):
       autotools = AutoToolsBuildEnvironment(self)
       with tools.chdir("./libsrtp-%s" % (self.version)):
           autotools.configure()
           autotools.make()

    def package(self):
       autotools = AutoToolsBuildEnvironment(self)
       with tools.chdir("./libsrtp-%s" % (self.version)):
           autotools.install()

    def package_info(self):
        self.cpp_info.libs = ["srtp2"]

