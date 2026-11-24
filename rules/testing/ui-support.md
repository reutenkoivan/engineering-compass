# UI test support

## Selectors and Page Objects

**Default:** select native locators/test IDs by semantic purpose/scope, not universal
role/label/test-ID precedence. CSS position needs a structural contract. **Invariant:**
Page test IDs have one Page-private dictionary shared by UI/Page Object; Tests use
semantic APIs, not copied IDs. Semantic locators need no dictionary. Independently
prove names/state/keyboard guarantees and scope repeated instances. No global registry,
ID-per-node or stripping is prescribed. Account for any changes to interaction,
roles or presentation meaning when editing selectors.

**Invariant:** Page Objects follow semantic Page parts and expose actions/native handles,
including root navigation. They need not mirror private DOM/region/view trees or expose
both an action and a handle for every element. **Default:** use semantic interaction names, such as
`app.page.editor.toolbar.save()`. **Invariant:** Page Objects never assert, return
pass/fail or hide proof behind `verifySaved`. Observable readiness supports actions,
not the oracle; arbitrary sleeps prove no readiness. Keep private Page support;
extract sections only for independent responsibilities. Widgets need no automatic
Page Object/artificial Page, production barrel, production test dependency or Page
Object test suite.

## Stories and support boundaries

**Contextual choice:** Stories are optional Page-owned projections for concrete docs,
visual or accessibility consumers; they mandate no Storybook. Project canonical Case
inputs/outcomes into UI. Tool render configuration/providers belong to that projection,
not a second semantic Case tree. Stories own no Scenario identity/actions/expectations/
proof; rendering proves no transition/reachability. Tests can reuse render config but
own action/observation/proof. Reference another owner's Case without copying it.
Widget-owned Stories need concrete justification. Under the UI rules, environment
providers do not make controlled templates uncontrolled.

**Default:** Page-relative support uses `test/page-object.ts`,
`stories/<presentation>.stories.tsx` and `test-ids.ts` in existing private support,
or `internal/test-ids.ts` under the applicable [Code module rules](../code/modules.md). Cases/Tests keep their semantic owners.
Dictionaries cannot make UI import test composition. Keep one Page Object file when
sufficient; under those module rules, migration uses `test/page-object/index.ts` and removes
the old file. Split Stories by coherent presentation, not State/Check count. `test`
and `stories` are classifications and need no barrel; tool-fixed paths may prevail with ownership
preserved. Verify support is not collected as Tests; paths mandate no repository migration.

**Invariant:** production UI may import plain selector data, not Page Objects, runner
fixtures or Stories. Fixtures compose Page Objects; Tests use Cases and own proof;
Stories compose Cases/rendering through narrow interfaces. Importing Case data registers
no Tests/lifecycle; executable Tests are not Case entries. Production/runner/Story
environments remain distinct with actual dependencies for each consumer. JSON is not
required. Page-private ownership grants no cross-package private access: use allowed
entries even in private workspaces; agree external testing APIs as contracts. Check
entries/dependencies/discovery/artifacts for accidental runner/Story exposure through
broad mappings. Deliberate Story builds are distinct artifacts; production markup may
retain IDs, and archived source is not automatically public. No mandatory stripping
checker or declaration suite follows.
