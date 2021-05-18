import json
import boto3


class Modify_Rds_Instances:

    def __init__(self):
        authentication = boto3.session.Session(profile_name="piee-test")
        self.rds_client = authentication.client('rds')
        self.list_of_dbs = []
        self.list_of_engines = []
        self.list_of_engine_versions = []

    def describe_db_instances(self):
        # call the describe db instances method from within the RDS module
        response = self.rds_client.describe_db_instances()

        # filter out required values from the response
        for instance in response['DBInstances']:
            self.list_of_dbs.append(instance['DBInstanceIdentifier'])
            self.list_of_engines.append(instance['Engine'])
            self.list_of_engine_versions.append(instance['EngineVersion'])

        for dbName, engineName, engineVersion in zip(self.list_of_dbs, self.list_of_engines,
                                                     self.list_of_engine_versions):
            describe_engine_versions = self.rds_client.describe_db_engine_versions(
                Engine=engineName,
                EngineVersion=engineVersion)

            for engines in describe_engine_versions['DBEngineVersions']:
                print("\nDB Name: " + dbName)
                print("Engine: " + engines['Engine'])
                print("Current Version: " + engines['EngineVersion'])

                count = 0
                while count < 1:
                    print("Available versions to upgrade to: ")
                    count += 1

                for availableVersions in engines['ValidUpgradeTarget']:
                    print(availableVersions['EngineVersion'])

    def update_db_instances(self):
        update_to_version = "14.00.3356.20.v1"
        for engine_versions in self.list_of_engine_versions:
            # if engine_versions[0:2] == "15":
            print("TESTING........")
            print(engine_versions)
            # for dbs in self.list_of_dbs:
        #         pass
        #     else:
        #         self.rds_client.modify_db_instance(DBInstanceIdentifier=dbs,
        #                                            # AllowMajorVersionUpgrade=False,
        #                                            # AutoMinorVersionUpgrade=True,
        #                                            EngineVersion=update_to_version,
        #                                            ApplyImmediately=True)
        # print(f"Updating to version: {update_to_version}")


def lambda_handler():
    instances = Modify_Rds_Instances()
    instances.describe_db_instances()
    instances.update_db_instances()


lambda_handler()

# import json
# import boto3
#
#
# class Modify_Rds_Instances:
#
#     def __init__(self):
#         authentication = boto3.session.Session(profile_name="piee-test")
#         self.rds_client = authentication.client('rds')
#         self.list_of_dbs = []
#         self.list_of_engines = []
#         self.list_of_engine_versions = []
#
#     def describe_db_instances(self):
#         # call the describe db instances method from within the RDS module
#         response = self.rds_client.describe_db_instances()
#
#         # filter out required values from the response
#         for instance in response['DBInstances']:
#             self.list_of_dbs.append(instance['DBInstanceIdentifier'])
#             self.list_of_engines.append(instance['Engine'])
#             self.list_of_engine_versions.append(instance['EngineVersion'])
#
#         for dbName, engineName, engineVersion in zip(self.list_of_dbs, self.list_of_engines,
#                                                      self.list_of_engine_versions):
#             describe_engine_versions = self.rds_client.describe_db_engine_versions(
#                 Engine=engineName,
#                 EngineVersion=engineVersion)
#
#             for engines in describe_engine_versions['DBEngineVersions']:
#                 print("\nDB Name: " + dbName)
#                 print("Engine: " + engines['Engine'])
#                 print("Current Version: " + engines['EngineVersion'])
#
#                 count = 0
#                 while count < 1:
#                     print("Available versions to upgrade to: ")
#                     count += 1
#
#                 for availableVersions in engines['ValidUpgradeTarget']:
#                     print(availableVersions['EngineVersion'])
#                     # testing.append(availableVersions['EngineVersion'])
#
#     def update_db_instances(self):
#         update_to_version = "14.00.3294.2.v1"
#         for dbs in self.list_of_dbs:
#             self.rds_client.modify_db_instance(DBInstanceIdentifier=dbs,
#                                                # AllowMajorVersionUpgrade=False,
#                                                # AutoMinorVersionUpgrade=True,
#                                                EngineVersion=update_to_version,
#                                                ApplyImmediately=True)
#
#
# def lambda_handler():
#     instances = Modify_Rds_Instances()
#     instances.describe_db_instances()
#     # instances.update_db_instances()
#
#
# lambda_handler()


# import json
# import boto3
#
#
# class Modify_Rds_Instances:
#
#     def __init__(self):
#         authentication = boto3.session.Session(profile_name="piee-test")
#         self.rds_client = authentication.client('rds')
#         self.list_of_dbs = []
#         self.list_of_engines = []
#         self.list_of_engine_versions = []
#
#     def describe_db_instances(self):
#         # call the describe db instances method from within the RDS module
#         response = self.rds_client.describe_db_instances()
#
#         # filter out required values from the response
#         for instance in response['DBInstances']:
#             self.list_of_dbs.append(instance['DBInstanceIdentifier'])
#             self.list_of_engines.append(instance['Engine'])
#             self.list_of_engine_versions.append(instance['EngineVersion'])
#
#         for dbName, engineName, engineVersion in zip(self.list_of_dbs, self.list_of_engines,
#                                                      self.list_of_engine_versions):
#             describe_engine_versions = self.rds_client.describe_db_engine_versions(
#                 Engine=engineName,
#                 EngineVersion=engineVersion)
#
#             for engines in describe_engine_versions['DBEngineVersions']:
#                 print("\nDB Name: " + dbName)
#                 print("Engine: " + engines['Engine'])
#                 print("Current Version: " + engines['EngineVersion'])
#
#                 count = 0
#                 while count < 1:
#                     print("Available versions to upgrade to: ")
#                     count += 1
#
#                 for availableVersions in engines['ValidUpgradeTarget']:
#                     print(availableVersions['EngineVersion'])
#                     # testing.append(availableVersions['EngineVersion'])
#
#     def update_db_instances(self):
#         update_to_version = "14.00.3356.20.v1"
#         for dbs in self.list_of_dbs:
#             if self.list_of_engine_versions[0:1] == "14":
#                 print("TESTING........")
#         pass
#     else:
#         self.rds_client.modify_db_instance(DBInstanceIdentifier=dbs,
#                                            # AllowMajorVersionUpgrade=False,
#                                            # AutoMinorVersionUpgrade=True,
#                                            EngineVersion=update_to_version,
#                                            ApplyImmediately=True)
# print(f"Updating to version: {update_to_version}")
