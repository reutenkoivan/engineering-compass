# Engineering Compass release map

Read this map from the verified installed target. Each row identifies a release,
its immediate predecessor, and migration files introduced in that release.
The map lists published releases in forward order. Use versioned rows starting
at `0.1.0` to select a migration path. The earlier rows record published sources
for adoption audits and historical prerequisite evidence.

| Release | Previous release | Migration files |
| --- | --- | --- |
| `d1c5f8c53ac68ae052e671348737eaed264c24bb` | — | — |
| `720ef1f62a4aaaf2fd192768f064cd56db6994c9` | `d1c5f8c53ac68ae052e671348737eaed264c24bb` | — |
| `626fe73e239bda03106e447db9e43de5f9c2f7d6` | `720ef1f62a4aaaf2fd192768f064cd56db6994c9` | — |
| `0.1.0` | `626fe73e239bda03106e447db9e43de5f9c2f7d6` | [record-approved-revision.md](migrations/record-approved-revision.md) |
| `0.2.0` | `0.1.0` | [migrate-to-release-channel.md](migrations/migrate-to-release-channel.md) |
| `0.3.0` | `0.2.0` | [use-active-global-version.md](migrations/use-active-global-version.md) |
