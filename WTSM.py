def Credits():
    ## Credits for Creator + Version Number (Example v3.2.2)
    global version, developer
    version = "v2.0.0"
    developer = "YT*Toaster (James Mc'Douglas)"
    return version, developer
Credits()


def Backup():
    from shutil import copytree
    from os import path, getcwd, makedirs, getenv

    directory = getcwd()
    app_datadir = getenv("LOCALAPPDATA")

    plugins_dir = path.join(directory,'_dat','MMplugins')
    backups_dir = path.join(directory,'_dat','_backups')
    isz_sav_dir = path.join(app_datadir,'ISZ','Saved','SaveGames')

    if path.exists(backups_dir):
        print("CONSOLE: Unable To Backup Current Save-Data.")
    else:
        print("CONSOLE: Backed-Up Current Save-Data.")
        makedirs(backups_dir, exist_ok=True)
        copytree(isz_sav_dir,f'{backups_dir}\\SaveGames')

def Inject():
    from shutil import copytree, rmtree
    from os import path, getenv, getcwd

    directory = getcwd()
    app_datadir = getenv("LOCALAPPDATA")

    plugins_dir = path.join(directory,'_dat','MMplugins')
    backups_dir = path.join(directory,'_dat','_backups','SaveGames')
    isz_sav_dir = path.join(app_datadir,'ISZ','Saved')
    write2_dir = path.join(isz_sav_dir,'SaveGames')

    if path.exists(write2_dir):
        rmtree(write2_dir)
        copytree(backups_dir,f'{isz_sav_dir}\\SaveGames')
        print("CONSOLE: Injected Save-Data.")
    else:
        copytree(backups_dir,f'{isz_sav_dir}\\SaveGames')
        print("CONSOLE: Injected Save-Data.")

    

def error():
    print("WARNING: If you are seeing this, the Plugin isn't a Correct Name.")
    print("WARNING: This plugin is partnered will the 'ISZ-ModMenu'. *It should be named: 'WTSM'.")
    print(" ")
    print("WARNING: As such we have special functionality for Backups and Injecting.")
    print("WARNING: Which do not work with Traditional Plugins.")


def MainApp():
    ## Your Code Here.
    error()