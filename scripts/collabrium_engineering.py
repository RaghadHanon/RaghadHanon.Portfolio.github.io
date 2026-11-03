"""Collabrium's backend, explained through its reviewed implementation."""
from components import *
from urllib.parse import quote

SNAPSHOT = '01aa3dd11fe0b888f54de64314ec3ca2aeb4ca1a'
REPO = GITHUB + '/Collabrium'


def source(path, label='Read the implementation', fragment=''):
    return ext(REPO + '/blob/' + SNAPSHOT + '/' + quote(path, safe='/') + fragment, label, 'ce-source')


MODULES = [
    ('auth', 'Organization', 'Authentication & accounts', 'From the first invitation to session renewal.',
     ['Super Admin and tenant-employee registration; email confirmation and confirmation resend.',
      'Email/password login, access tokens, persisted refresh tokens, rotation and explicit revocation.',
      'Password recovery, password reset and authenticated password change.',
      'First-login password-change state is exposed to the client and enforced through a policy.'],
     ['/api/auth'], ['API/Controllers/AuthController.cs', 'Infrastructure/Identity/IdentityService.cs']),
    ('tenants', 'Organization', 'Tenant administration', 'An organization is a first-class boundary.',
     ['Register a tenant with its administrator; browse, search, filter and inspect organizations.',
      'Maintain organization profiles, contact details, social links and branding.',
      'Activate or deactivate tenants and retrieve tenant users and summary information.',
      'Resolve the platform-wide global tenant for Super Admin operations.'],
     ['/api/tenants'], ['API/Controllers/TenantsController.cs', 'Domain/Models/Tenant.cs']),
    ('users', 'Organization', 'Users & skills', 'People, account state and skills in one tenant context.',
     ['Current-user and authorized user profiles, profile updates and image uploads.',
      'Add, inspect and remove personal skills; inspect other users’ skills where authorized.',
      'Role changes, activation changes, manager lookup and assignable-user selection.',
      'Skill data connects the organization model to AI-assisted development recommendations.'],
     ['/api/users'], ['API/Controllers/UsersController.cs', 'Domain/Models/User.cs']),
    ('teams', 'Organization', 'Team management', 'Membership carries business meaning.',
     ['Create, edit, search, sort and paginate teams; retrieve teams for a user.',
      'Candidate-member selection, membership changes, leadership and activation.',
      'The domain protects capacity, duplicate membership and the current team lead.',
      'Team membership supports project access, course assignment and notification audiences.'],
     ['/api/teams'], ['API/Controllers/TeamsController.cs', 'Domain/Models/Team.cs']),
    ('projects', 'Delivery', 'Project management', 'Planning, responsibility and a traceable delivery history.',
     ['Create and maintain projects with validated keys, planned dates and lifecycle status.',
      'Assign or unassign a team; retrieve projects available to the current user.',
      'Backlogs, boards, Epic and User Story views, plus project history.',
      'Project access combines tenant ownership, elevated roles and project membership.'],
     ['/api/projects'], ['API/Controllers/ProjectsController.cs', 'Domain/Models/Project.cs']),
    ('work-items', 'Delivery', 'Work-item management', 'Five specialized models with connected quality rules.',
     ['Epics, User Stories, Tasks, Bugs and Test Cases with type-specific fields and workflows.',
      'Assignment, priority, blocked state, sprint movement and linked-work validation.',
      'Comments, attachments, code links, relation candidates and change history.',
      'Parent, Child, RelatesTo and Bug-to-Test-Case traceability through FoundByTestCase.',
      'User Story release gates inspect linked task completion, open bugs and test outcomes.'],
     ['/api/projects/{projectId}/work-items'], ['API/Controllers/WorkItemsController.cs', 'Domain/Models/WorkItem.cs']),
    ('sprints', 'Delivery', 'Sprint management', 'Planned dates and actual execution are separate.',
     ['Create, schedule, edit and inspect sprints; manage their work-item scope.',
      'Start a Planned sprint, complete an Active sprint, or cancel an eligible sprint.',
      'Completion returns unfinished work to the backlog while keeping Done work in the sprint.',
      'Sprint history, delivery metrics and status-change notifications use the same execution data.'],
     ['/api/projects/project/{projectId}/sprints'], ['API/Controllers/SprintsController.cs', 'Application/Features/Sprints/Commands/CompleteSprint.cs']),
    ('learning', 'Learning & community', 'Learning Hub', 'Content, assignments and individual progress connect.',
     ['Courses with providers, levels, languages, tags, learning points, thumbnails and ratings.',
      'Save courses, assign them to users or teams, and track NotStarted, InProgress and Completed states.',
      'Assigned, saved and personal-course views, learner summaries and assignment statistics.',
      'Roadmaps with publishing, visibility, tags, ordered Topic/Reference nodes, subtopics and resources.',
      'Articles with publishing, covers, tags, comments and likes.',
      'AI-generated roadmap drafts and topic, subtopic and resource suggestions.'],
     ['/api/courses', '/api/user-courses', '/api/user-course-assignments', '/api/roadmaps', '/api/articles'],
     ['API/Controllers/UserCoursesController.cs', 'API/Controllers/RoadmapsController.cs', 'Domain/Models/UserCourse.cs']),
    ('community', 'Learning & community', 'Community Hub', 'Internal knowledge and organization-wide communication.',
     ['General, Question, Discussion, Resource and Tip posts, with tags, images, comments and likes.',
      'Pin important posts; Resource posts can carry links under explicit collection limits.',
      'Online and in-person events, calendar views, banners, cancellation and attendance.',
      'Capacity checks and duplicate-attendance prevention, reinforced by a database unique index.',
      'Announcements with priorities, publication/expiry times and Everyone, Team or Role audiences.'],
     ['/api/posts', '/api/events', '/api/announcements'],
     ['API/Controllers/PostsController.cs', 'Domain/Models/Event.cs', 'Domain/Models/Announcement.cs']),
    ('notifications', 'Platform & insights', 'Notification center', 'Persistent messages, followed by live delivery.',
     ['Paged personal notifications, unread counts, mark-one-read and mark-all-read operations.',
      'Recipient, tenant, triggering user, related entity and action URL are retained with each message.',
      'Application-event handlers create notifications for account, team, work, learning and community activity.',
      'SignalR delivers NotificationReceived and UnreadCountChanged after notification persistence.',
      'Application events also connect relevant work, team, account and course operations to template-based SMTP email.'],
     ['/api/notifications', '/hubs/notifications'],
     ['API/Controllers/NotificationsController.cs', 'Application/Services/NotificationCreationService.cs']),
    ('reports', 'Platform & insights', 'Reports & analytics', 'One metric model, several useful representations.',
     ['Ten report types covering the tenant, sprint progress, velocity, cycle time, bugs, productivity and project health.',
      'Structured JSON results, ScottPlot charts and branded QuestPDF document exports.',
      'Sprint summaries complement the report-type workflow.',
      'AI insight generation starts with the selected report’s retrieved application data.'],
     ['/api/reports'], ['API/Controllers/ReportsController.cs', 'Infrastructure/Persistence/ReadModels/ReportsReadModel.cs']),
    ('ai', 'Platform & insights', 'AI assistance', 'Suggestions and drafts inside the application’s boundaries.',
     ['Suggested fields for all five concrete work-item types.',
      'Full roadmap drafts, generation-and-create workflows, and topic/subtopic/resource suggestions.',
      'Current-user skill-gap analysis based on the recorded role and skills.',
      'Report insights containing summaries, findings, risks and recommendations.',
      'Ollama/Gemma 3 integration with structured parsing, normalization, output-repair attempts and service-specific fallbacks.'],
     ['/api/ai/roadmaps', '/api/ai/reports', '/api/Gaps/skill-gaps/me'],
     ['Infrastructure/AI/OllamaAiAssistantService.cs', 'Infrastructure/AI/WorkItemFieldsSuggestionService.cs']),
    ('metadata', 'Platform & insights', 'Metadata & shared options', 'The API publishes the vocabulary the UI works with.',
     ['Domain enums for roles, work-item types, statuses, priorities, departments and more.',
      'Work-item workflow metadata and relation rules.',
      'Course, roadmap, post and announcement options.',
      'Shared tag creation, lookup, search, updates and deletion.'],
     ['/api/metadata', '/api/tags'], ['API/Controllers/MetadataController.cs', 'API/Controllers/TagsController.cs']),
]


def module_catalog():
    filters = ['All', 'Organization', 'Delivery', 'Learning & community', 'Platform & insights']
    controls = ''.join(f'<button type="button" data-ce-filter="{escape(c, quote=True)}" aria-pressed="{str(c == "All").lower()}">{escape(c)}</button>' for c in filters)
    entries = []
    for i, (id, group, title, summary, features, routes, paths) in enumerate(MODULES):
        search = ' '.join([title, group, summary, *features, *routes]).lower()
        entries.append(f'''<details class="ce-module" id="module-{id}" data-ce-module data-ce-group="{escape(group, quote=True)}" data-ce-search="{escape(search, quote=True)}"><summary><span class="ce-index mono">{i+1:02}</span><span><small>{escape(group)}</small><strong>{escape(title)}</strong><span>{escape(summary)}</span></span><span class="ce-plus" aria-hidden="true">+</span></summary><div class="ce-module-body"><ul>{''.join('<li>'+escape(f)+'</li>' for f in features)}</ul><div class="ce-routes">{''.join('<code>'+escape(r)+'</code>' for r in routes)}</div><div class="ce-sources">{''.join(source(p, Path(p).name) for p in paths)}</div></div></details>''')
    return f'''<div class="ce-module-tools" data-ce-controls hidden><label for="ce-search">Find a capability <input id="ce-search" type="search" placeholder="Try: email, roadmap, tests, assignment…" autocomplete="off" aria-controls="ce-modules"></label><div class="ce-filters" role="group" aria-label="Filter Collabrium modules">{controls}</div><p id="ce-module-count" class="ce-small" role="status" aria-live="polite">13 of 13 modules</p></div><div id="ce-modules" class="ce-modules">{''.join(entries)}</div><p class="ce-empty" id="ce-no-results" hidden>No modules match. Try another term or choose All.</p>'''


FLOWS = [
    ('create', 'Create a work item', 'A business operation spanning several records.', [
        ('API contract', 'A type-specific endpoint maps the transport request into a MediatR command.'),
        ('Tenant & project', 'The handler resolves tenant context, project and current user before creating work.'),
        ('Domain construction', 'A C# switch selects Epic, UserStory, TaskItem, Bug or TestCase and validates the required type-specific details.'),
        ('One transaction', 'The project counter supplies the next code. The new work item, updated counter and creation history are saved through the Unit of Work.'),
        ('Result', 'The handler returns the new identifier with Created status.')],
     ['Application/Features/WorkItems/Commands/CreateWorkItem.cs', 'Infrastructure/Persistence/UnitOfWork.cs']),
    ('assign', 'Assign work & notify', 'The saved change and its delivery channels have distinct responsibilities.', [
        ('Resolve the resource', 'Load the work item inside the requested tenant and project.'),
        ('Check the actor & target', 'Apply manager/creator/self-assignment rules and confirm that the target user has project access.'),
        ('Commit the change', 'Update the assignee and record before/after history in one database transaction.'),
        ('Publish an application event', 'After that transaction, publish WorkItemAssignedEvent through MediatR.'),
        ('Deliver through handlers', 'One handler builds a template-based SMTP email. Another persists an in-app notification, then sends SignalR notification and unread-count updates.')],
     ['Application/Features/WorkItems/Commands/UpdateWorkItemAssignee.cs', 'Application/EventsHandlers/WorkItemAssignedEmailHandler.cs', 'Application/Services/NotificationCreationService.cs']),
    ('status', 'Move work through delivery', 'The caller, project, sprint and linked work all matter.', [
        ('Load context', 'Retrieve the project, work item, current user and linked work in the tenant scope.'),
        ('Authorize the change', 'Require an assignee, reject blocked items and permit a manager or the current assignee.'),
        ('Apply domain behavior', 'The concrete work-item type validates transitions. Project state and an Active sprint are required; User Story testing/release gates inspect linked work.'),
        ('Persist with history', 'Update the item and record the change within the Unit of Work transaction.'),
        ('Return the read model', 'Reload the DTO, including the status options the client can present.')],
     ['Application/Features/WorkItems/Commands/UpdateWorkItemStatus.cs', 'Domain/Models/UserStory.cs']),
    ('sprint', 'Complete a sprint', 'Keep delivery history useful after the sprint closes.', [
        ('Validate the lifecycle', 'The use case resolves the tenant, user, project and sprint, then requires an Active sprint.'),
        ('Return incomplete scope', 'Unfinished work moves back to the backlog; Done items stay attached to the completed sprint.'),
        ('Commit completion', 'The domain records the actual completion timestamp. Sprint changes and history are saved in the same transaction.'),
        ('Notify the team', 'If the project has an assigned team, publish SprintStatusChangedEvent for the relevant team members.'),
        ('Preserve reporting context', 'Completed sprint work remains available to sprint and velocity reporting.')],
     ['Application/Features/Sprints/Commands/CompleteSprint.cs', 'Infrastructure/Persistence/ReadModels/ReportsReadModel.cs']),
    ('learning', 'Assign learning without losing progress', 'Content and the employee’s relationship to it are separate models.', [
        ('Resolve course & users', 'Check the current tenant, course, assigning user and target user.'),
        ('Apply assignment rules', 'Reject self-assignment and the target roles blocked by CourseAssignmentRules.'),
        ('Create or update UserCourse', 'Assign the course while keeping personal saved state and progress distinct.'),
        ('Commit & publish', 'Persist the relationship, then publish CourseAssignedEvent for email and in-app notification handlers.'),
        ('Retain useful learning history', 'On unassignment, retain a saved or started record. Delete only a record that has no saved state or learning activity.')],
     ['Application/Features/UserCourses/Commands/AssignCourseToUser.cs', 'Domain/Models/UserCourse.cs']),
    ('ai-roadmap', 'Generate & save a roadmap', 'Generated structure goes through ordinary domain and persistence rules.', [
        ('Collect a goal', 'The command accepts path, level, goal and requested topic/subtopic counts.'),
        ('Generate a structured draft', 'The Ollama-backed draft service parses and normalizes model output, repairs unusable responses and provides a fallback draft when needed.'),
        ('Construct domain objects', 'Create Roadmap, TopicNode and RoadmapSubTopic objects from the accepted draft, in order.'),
        ('Save the structure atomically', 'Repositories persist the roadmap hierarchy inside a Unit of Work transaction.'),
        ('Return application data', 'Reload the roadmap details through its read model for the client.')],
     ['Application/Features/Roadmaps/Commands/CreateRoadmapWithAi.cs', 'Infrastructure/AI/RoadmapAiDraftService.cs']),
]


def workflow_explorer():
    items = []
    for i, (id, title, intro, steps, paths) in enumerate(FLOWS):
        items.append(f'''<details class="ce-workflow" {'open' if i == 0 else ''}><summary><span class="ce-index mono">{i+1:02}</span><span><strong>{escape(title)}</strong><small>{escape(intro)}</small></span><span class="ce-plus" aria-hidden="true">+</span></summary><div class="ce-workflow-body"><ol class="ce-steps">{''.join('<li><strong>'+escape(t)+'</strong><p>'+escape(p)+'</p></li>' for t,p in steps)}</ol><div class="ce-sources">{''.join(source(p,Path(p).name) for p in paths)}</div></div></details>''')
    return ''.join(items)


ARCHITECTURE_MAP = '''<figure class="ce-system-map"><div class="ce-map-scroll" tabindex="0" aria-label="Architecture diagram; scroll horizontally on small screens"><svg viewBox="0 0 960 370" role="img" aria-labelledby="ce-map-title ce-map-description"><title id="ce-map-title">The four backend projects and their dependencies</title><desc id="ce-map-description">API references Application and Infrastructure. Application references Domain. Infrastructure references and implements abstractions in Application.</desc><g font-family="Manrope,Arial"><rect x="30" y="45" width="230" height="112" rx="12" fill="#344137" stroke="#6b7b66"/><text x="52" y="74" fill="#c4cfba" font-size="11">HTTP &amp; COMPOSITION</text><text x="52" y="109" fill="#fff3e8" font-size="27">API</text><text x="52" y="135" fill="#c4cfba" font-size="12">Contracts · Controllers · Policies</text><rect x="350" y="45" width="250" height="112" rx="12" fill="#344137" stroke="#9eae90"/><text x="372" y="74" fill="#c4cfba" font-size="11">USE CASES &amp; PORTS</text><text x="372" y="109" fill="#fff3e8" font-size="27">Application</text><text x="372" y="135" fill="#c4cfba" font-size="12">Commands · Queries · Events</text><rect x="700" y="45" width="230" height="112" rx="12" fill="#b84d2e"/><text x="722" y="74" fill="#fff3e8" font-size="11">BUSINESS BEHAVIOR</text><text x="722" y="109" fill="#fff3e8" font-size="27">Domain</text><text x="722" y="135" fill="#fff3e8" font-size="12">Models · Guards · Value objects</text><rect x="350" y="245" width="350" height="100" rx="12" fill="#28332b" stroke="#6b7b66"/><text x="373" y="282" fill="#fff3e8" font-size="25">Infrastructure</text><text x="373" y="309" fill="#c4cfba" font-size="12">EF Core · Identity · SignalR · SMTP · AI</text><g fill="none" stroke="#adbaa5" stroke-width="1.5"><path d="M270 101H336M610 101H686M475 232V171M145 171v125h191"/><path d="m328 95 8 6-8 6m350-12 8 6-8 6M469 179l6-8 6 8M328 290l8 6-8 6"/></g><text x="495" y="204" fill="#c4cfba" font-size="11">implements application interfaces</text><text x="166" y="274" fill="#c4cfba" font-size="11">composes</text></g></svg></div><figcaption>Arrows show project dependencies. The composition root wires application interfaces to infrastructure implementations.</figcaption></figure>'''


def architecture_section():
    layers = [
        ('API', 'A deliberate HTTP boundary', 'Controllers map request contracts to application messages. AutoMapper, transport validators, JSON configuration, authorization policies and Problem Details keep the external API explicit.', 'API/SetupProgram/ServiceCollectionExtensions.cs'),
        ('Application', 'Feature-oriented use cases', 'Commands coordinate mutations through repositories and domain behavior. Queries use dedicated read-model interfaces. MediatR dispatches requests and application events, with a shared FluentValidation behavior.', 'Application/DependencyInjection.cs'),
        ('Domain', 'Rules expressed as behavior', 'Projects, sprints, work items, teams, learning content and community models encapsulate invariants and state changes. Concrete work-item types override their permitted transitions and completion rules.', 'Domain/Models/WorkItem.cs'),
        ('Infrastructure', 'Implementations behind interfaces', 'EF Core and SQL Server, explicit domain/entity mappers, Identity/JWT, SMTP, Cloudinary, SignalR, AI services, report renderers and hosted workers provide the technical implementations.', 'Infrastructure/DependencyInjection.cs'),
    ]
    cards = ''.join(f'<article class="ce-layer"><span class="label">{a}</span><h3>{b}</h3><p>{c}</p>{source(d)}</article>' for a,b,c,d in layers)
    return ARCHITECTURE_MAP + '<div class="ce-layer-grid">' + cards + '''</div><div class="ce-path-pair"><article><span class="label">Command side</span><h3>Protect the operation.</h3><p>Validate the request, load a domain model, apply behavior, persist through repositories and commit related changes with the Unit of Work.</p></article><article><span class="label">Query side</span><h3>Return what the screen needs.</h3><p>Use dedicated read models, filtering, DTO projections, no-tracking reads and pagination where implemented. Read and write models share SQL Server; CQRS here does not imply separate databases.</p></article></div>'''


def domain_section():
    workflow_rows = [
        ('Epic', ['ToDo','InProgress','Done'], 'Done requires linked User Stories to be Done.'),
        ('User Story', ['ToDo','ReadyForDev','InProgress','InReview','InTesting','ReadyForRelease','Done'], 'Testing requires completed linked Tasks. Release/Done additionally require closed linked Bugs and completed, passed Test Cases.'),
        ('Task', ['ToDo','ReadyForDev','InProgress','InReview','Done'], 'Concrete transitions support development, review and rework.'),
        ('Bug', ['ToDo','ReadyForDev','InProgress','InTesting','Done'], 'Defect-oriented transitions include retesting and reopening.'),
        ('Test Case', ['ToDo','InTesting','Done'], 'Record an outcome while InTesting; the status-change use case requires Passed before Done.'),
    ]
    table = ''.join(f'<tr><th scope="row">{name}</th><td><div class="ce-state-set">'+''.join('<code>'+s+'</code>' for s in states)+f'</div></td><td>{rule}</td></tr>' for name,states,rule in workflow_rows)
    rules = [
        ('Hierarchy has a shape', 'An Epic contains User Stories; a User Story can contain Tasks, Bugs and Test Cases. Relation rules reject self-links, duplicate relations and invalid parent/child type pairs. FoundByTestCase is a Bug-to-Test-Case relation.', 'Domain/Models/WorkItem.cs'),
        ('Related scope moves together', 'The update workflow moves a User Story’s Task/Bug/Test Case children with it. A child cannot move to a different sprint from its User Story. This same-sprint rule does not extend to the Epic–User Story relationship.', 'Application/Features/WorkItems/Commands/UpdateWorkItem.cs'),
        ('Execution has preconditions', 'The status command requires an assignee and rejects blocked work. The domain requires an eligible project state and an Active sprint, validates the concrete transition, and records execution timestamps.', 'Application/Features/WorkItems/Commands/UpdateWorkItemStatus.cs'),
        ('Planning uses a defined vocabulary', 'User Story estimates accept 1, 2, 3, 5, 8 or 13 points. Projects generate sequential work-item codes and sprint names. Sprint planned dates remain distinct from actual start and completion times.', 'Domain/Models/UserStory.cs'),
        ('Learning history survives assignment changes', 'Saved state, assignment and progress are independent. Unassigning clears assignment metadata; a saved, started or completed record is retained instead of losing the learner’s history.', 'Domain/Models/UserCourse.cs'),
        ('Organization and community have rules too', 'Team models protect lead membership and capacity. Event registration checks capacity and duplicate attendance. Announcement audiences validate their target shape, while community posts restrict links to Resource posts.', 'Domain/Models/Team.cs'),
    ]
    detail = ''.join(f'<article class="ce-rule"><h3>{t}</h3><p>{p}</p>{source(s)}</article>' for t,p,s in rules)
    return '''<div class="ce-hierarchy" aria-label="Work hierarchy"><span>Epic</span><span>User Story</span><div><span>Task</span><span>Bug</span><span>Test Case</span></div></div><div class="ce-table-scroll" tabindex="0" aria-label="Work-item workflow table"><table class="ce-table"><caption>State sets exposed by workflow metadata</caption><thead><tr><th scope="col">Work item</th><th scope="col">Canonical states</th><th scope="col">A meaningful rule</th></tr></thead><tbody>''' + table + '''</tbody></table></div><p class="ce-small">These are state sets, not one universal linear sequence. Each concrete model validates its own transitions.</p><div class="ce-rule-grid">''' + detail + '</div><div class="ce-sources">' + source('Application/Features/Metadata/Queries/GetWorkItemsWorkFlowMetadata.cs', 'Workflow metadata') + source('Domain/Models/WorkItem.cs','Domain relationship rules') + '</div>'


def security_section():
    layers = [
        ('Identity', 'ASP.NET Core Identity validates credentials and email confirmation, issues access tokens and persists rotating refresh tokens. First-login password-change state is part of the account lifecycle.'),
        ('Tenant context', 'For ordinary tenant-aware HTTP requests, middleware validates the authenticated user, account activation, tenant claim, tenant activation and membership. Super Admin uses a global tenant context.'),
        ('Operation policy', 'Named policies protect module operations. Project_Access separately verifies that the project belongs to the user’s tenant, then applies role and project-membership rules.'),
        ('Use case & domain', 'Handlers validate related resources, responsibility and assignment eligibility. Domain behavior protects invariants even after the request has crossed its transport boundary.'),
    ]
    roles = ['SuperAdmin','TenantAdmin','CEO','HR','ProductOwner','TeamLead','BackendDev','FrontendDev','FullStackDev','QA','BusinessAnalyst','Designer','IT']
    cards = ''.join(f'<li><span class="ce-index mono">{i+1:02}</span><div><h3>{t}</h3><p>{p}</p></div></li>' for i,(t,p) in enumerate(layers))
    return f'''<ol class="ce-security-layers">{cards}</ol><div class="ce-callout"><strong>A shared database, with application-enforced tenant boundaries.</strong><p>Tenant identifiers, scoped request context, resource checks and tenant-aware queries work together. Hub connections follow their own connection-context paths; HTTP tenant middleware explicitly skips hub routes.</p></div><div class="ce-role-box"><h3>13 organizational roles</h3><p>Roles express responsibility. Effective access still depends on policies, tenant context and resource checks.</p><div class="ce-state-set">{''.join('<code>'+r+'</code>' for r in roles)}</div></div><div class="ce-sources">{source('API/Middlewares/TentantMiddleware.cs','Tenant middleware')}{source('API/SetupProgram/AuthorizationExtensions.cs','Authorization policies')}{source('Infrastructure/Security/AuthRequirements/MustHaveProjectAccess.cs','Project access')}{source('Infrastructure/Identity/IdentityService.cs','Identity and refresh tokens')}</div>'''


def data_section():
    items = [
        ('Separate domain and persistence models', 'Explicit mappers reconstruct behavior-rich domain objects from EF entities and map changes back. API contracts remain distinct from both.', 'Infrastructure/Persistence/Mappers/WorkItemMapper.cs'),
        ('Transactions and history', 'The Unit of Work owns transaction, SaveChanges, commit and rollback. Creation, assignment, sprint completion and other multi-record operations use it to keep their database changes together.', 'Infrastructure/Persistence/UnitOfWork.cs'),
        ('Read models for real screens', 'Work-item lists, boards, backlogs and reports use purpose-specific read models. Queries apply scope, filtering and projection; cursor-based lists fetch pageSize + 1 to detect another page.', 'Infrastructure/Persistence/ReadModels/WorkItemsReadModel.cs'),
        ('Constraints and access paths', 'The work-item mapping declares inheritance discriminators and composite indexes for project/sprint, type, status, assignee and priority. Unique indexes protect course relationships, ratings and event attendance.', 'Infrastructure/Persistence/Configurations/WorkItemConfiguration.cs'),
        ('Consistent time and schema changes', 'AppDbContext applies UTC converters to DateTime fields. EF Core migrations and configurable startup migration/seeding support database evolution and initial role/global-tenant data.', 'Infrastructure/Persistence/AppDbContext.cs'),
        ('Explicit failures at the boundary', 'FluentValidation protects transport and application requests. JSON rejects unmapped members. Exception handling maps failures to Problem Details with trace identifiers and Development-only diagnostics.', 'API/Middlewares/GlobalExceptionHandler.cs'),
    ]
    return '<div class="ce-rule-grid">'+''.join(f'<article class="ce-rule"><h3>{t}</h3><p>{p}</p>{source(s)}</article>' for t,p,s in items)+'</div>'


def integration_section():
    hubs = [
        ('Presence', '/hubs/presence', 'Tenant-scoped online users and online/offline updates, backed by an in-memory presence tracker.', 'Infrastructure/SignalR/Hubs/PresenceHub.cs'),
        ('Comments', '/hubs/comments', 'A connection binds to a project/work item, resolves context, loads permitted comments and broadcasts comment changes to that scope.', 'Infrastructure/SignalR/Hubs/CommentHub.cs'),
        ('Notifications', '/hubs/notifications', 'Connections join tenant, team and user groups. NotificationReceived and UnreadCountChanged keep the interface current.', 'Infrastructure/SignalR/Notifications/NotificationHub.cs'),
    ]
    hubcards = ''.join(f'<article class="ce-service"><h4>{name}</h4><code>{route}</code><p>{text}</p>{source(path)}</article>' for name,route,text,path in hubs)
    return f'''<div class="ce-integration-block"><div class="ce-integration-title"><span class="label">Live collaboration</span><h3>Three SignalR hubs.<br>Different connection scopes.</h3></div><div class="ce-service-grid">{hubcards}</div></div><div class="ce-integration-block"><div class="ce-integration-title"><span class="label">Events &amp; email</span><h3>One operation can reach<br>more than one channel.</h3></div><p>Work assignment, role changes, team membership, project assignment, sprint changes and course assignments publish application events. Dedicated handlers create in-app notifications or template-based SMTP email. Article/post interactions, announcements and event reminders also have notification handlers.</p><div class="ce-channel-grid"><article><h4>Persistent first</h4><p>NotificationCreationService saves recipient messages in a database transaction, then sends live messages and recalculates unread counts. Users can retrieve stored notifications after reconnecting.</p>{source('Application/Services/NotificationCreationService.cs')}</article><article><h4>SMTP and reusable templates</h4><p>EmailTemplateFactory resolves templates; EmailMessageBuilder assembles messages. SmtpEmailService sends HTML/plain-text content and supports attachments through System.Net.Mail with SSL enabled.</p>{source('Application/EventsHandlers/WorkItemAssignedEmailHandler.cs')}{source('Infrastructure/Email/SmtpEmailService.cs')}</article></div><p class="ce-small">These are in-process MediatR events. Database commits and external email/SignalR delivery are separate operations.</p></div><div class="ce-integration-block"><div class="ce-integration-title"><span class="label">Scheduled activity</span><h3>Two hosted workers.<br>Time-based business behavior.</h3></div><div class="ce-channel-grid"><article><h4>Announcement publication</h4><p>A BackgroundService with PeriodicTimer checks every minute for due announcements, publishes the notification event and records the processed state.</p>{source('Infrastructure/BackgroundServices/AnnouncementNotificationBackgroundService.cs')}</article><article><h4>Event reminders</h4><p>A second worker checks the upcoming 15-minute window, resolves attendees, publishes reminder notifications and records the sent state.</p>{source('Infrastructure/BackgroundServices/EventReminderBackgroundService.cs')}</article></div></div><div class="ce-integration-block"><div class="ce-integration-title"><span class="label">Media &amp; attachments</span><h3>Provider details stay<br>behind a storage interface.</h3></div><p>Cloudinary services handle profile images, branding, covers, banners, post media and work-item attachments. AttachmentStorageFactory selects image, video or file storage from the attachment type. Upload use cases check resource access before calling the provider; database transactions cover metadata and history.</p>{source('Infrastructure/FilesStorage/Factory/AttachmentStorageFactory.cs')}{source('Application/Features/WorkItems/Commands/Attachments/AddWorkItemAttachment.cs')}</div>'''


def ai_and_reports():
    reports = [
        ('TenantInfo', 'Organization, users, teams, projects, sprints and work summary.'),
        ('SprintProgress', 'Sprint scope and completion information.'),
        ('Velocity', 'Planned and completed User Story points across completed sprints.'),
        ('CycleTime', 'Completed work duration with average, median and range.'),
        ('BugSeverityDistribution', 'Bug distribution grouped by the recorded work-item priority.'),
        ('DeveloperProductivity', 'Developer-focused workload and completion metrics.'),
        ('TeamsProductivity', 'Team-level delivery and productivity information.'),
        ('BlockedWorkItems', 'Work currently marked as blocked.'),
        ('OverdueWorkItems', 'Work that is overdue according to its relevant dates.'),
        ('ProjectHealth', 'Combined project indicators and health classifications.'),
    ]
    rows = ''.join(f'<tr><th scope="row"><code>{name}</code></th><td>{description}</td></tr>' for name,description in reports)
    return f'''<div class="ce-ai-layout"><div><span class="label">Ollama / Gemma 3</span><h3>Useful assistance,<br>structured for the application.</h3><p>The HTTP integration calls an Ollama-compatible chat API with <code>gemma3:latest</code>. Feature services build prompts from the user’s input or retrieved application data and translate the response into typed DTOs.</p><ul class="ce-bullets"><li>Work-item field suggestions for Epics, User Stories, Tasks, Bugs and Test Cases.</li><li>Full roadmap drafts plus topic, subtopic and learning-resource suggestions.</li><li>Skill-gap analysis using the current user’s role and recorded skills.</li><li>Narrative insights generated from the requested report’s real data.</li></ul></div><div class="ce-ai-contract"><span class="label">A generated response crosses a boundary</span><ol><li><strong>Extract</strong><span>Recover the expected JSON from the model response.</span></li><li><strong>Normalize &amp; check</strong><span>Map to typed DTOs and inspect required fields and allowed values.</span></li><li><strong>Repair</strong><span>Work-item and full-roadmap services allow up to three output-generation attempts; other suggestion services use their own limits.</span></li><li><strong>Return or persist through a use case</strong><span>Suggestions return to the client. Generation-and-create constructs domain objects and saves them through the normal transaction boundary.</span></li></ol></div></div><div class="ce-sources">{source('Infrastructure/AI/WorkItemFieldsSuggestionService.cs','Structured suggestions')}{source('Infrastructure/AI/RoadmapAiDraftService.cs','Roadmap drafts')}{source('Infrastructure/AI/UserSkillGapAiService.cs','Skill-gap analysis')}{source('Infrastructure/AI/ReportAiInsightService.cs','Report-grounded insight')}</div><div class="ce-report-heading"><span class="label">Analytics / 10 report types</span><h3>From scoped data<br>to a decision-ready document.</h3><p>Analytical read models supply JSON data. ScottPlot renders charts, QuestPDF builds branded PDFs, and the AI insight service can reuse the selected report data. Sprint summaries are also exposed by the Reports controller.</p></div><div class="ce-table-scroll" tabindex="0" aria-label="Implemented report types"><table class="ce-table ce-report-table"><caption>ReportType enum and implemented reporting purposes</caption><thead><tr><th scope="col">Report</th><th scope="col">What it describes</th></tr></thead><tbody>{rows}</tbody></table></div><div class="ce-sources">{source('Domain/Enums/ReportType.cs','The ten report types')}{source('Infrastructure/Persistence/ReadModels/ReportsReadModel.cs','Analytical queries')}{source('Infrastructure/Reports/Velocity/VelocityReportDocument.cs','QuestPDF document')}{source('Infrastructure/Reports/Velocity/VelocityChartRenderer.cs','ScottPlot chart')}</div>'''


def code_gallery():
    evidence = json.loads((ROOT/'scripts/collabrium_evidence.json').read_text())
    cards = []
    for i, item in enumerate(evidence['examples']):
        cards.append(f'''<details class="ce-proof" {'open' if i == 0 else ''}><summary><span class="ce-index mono">{i+1:02}</span><span><small>{escape(item['skill'])}</small><strong>{escape(item['title'])}</strong></span><span class="ce-plus" aria-hidden="true">+</span></summary><div class="ce-proof-body"><p>{escape(item['explanation'])}</p><div class="code-window ce-code-window"><div class="code-header"><span>{escape(Path(item['path']).name)}</span><span>C# / {item['start_line']}–{item['end_line']}</span></div>{codeblock(item['code'])}</div><p class="ce-small">Exact source excerpt; indentation normalized.</p>{source(item['path'],'Open the exact source lines',f"#L{item['start_line']}-L{item['end_line']}")}</div></details>''')
    return '<div class="ce-proofs">'+''.join(cards)+'</div>'


def skills_section():
    items = [
        ('C# & domain modeling', 'Encapsulation, inheritance, overridden behavior, guards, value objects, pattern matching and typed state transitions.', '#domain-rules'),
        ('Application architecture', 'CQRS, MediatR request/notification handlers, dependency injection, interfaces, repositories, read models and Unit of Work.', '#system-map'),
        ('Data engineering', 'EF Core/SQL Server, DTO projections, LINQ, no-tracking reads, pagination, inheritance mapping, constraints, indexes and UTC normalization.', '#data-api'),
        ('Security engineering', 'Identity, JWT, refresh-token rotation, tenant context, roles, policies, project-access requirements and operation-specific checks.', '#security'),
        ('Connected backend workflows', 'Async/await, cancellation tokens, application events, persistent notifications, SignalR groups, SMTP templates and scheduled workers.', '#integrations'),
        ('AI & reporting integrations', 'HTTP service abstraction, structured model output, repair/fallback logic, analytical read models, ScottPlot charts and QuestPDF exports.', '#ai-reports'),
    ]
    cards = ''.join(f'<a class="ce-skill" href="{url}"><h3>{t}{arrow("right")}</h3><p>{p}</p></a>' for t,p,url in items)
    return f'''<div class="ce-skills">{cards}</div><details class="ce-tradeoffs"><summary>Engineering context &amp; the next iteration <span aria-hidden="true">+</span></summary><p>Collabrium is a four-person graduation project. This walkthrough describes the implementation in the linked source snapshot. Application events and the presence tracker run in-process. A multi-instance evolution would need distributed presence/SignalR scale-out and a durable approach to background delivery.</p><p>The current repository contains no automated unit/integration test project or deployment pipeline. Domain-transition tests, tenant/authorization integration tests and notification-delivery tests are concrete next steps; no coverage or performance result is claimed here.</p>{source('README.md','Repository status and design notes')}</details>'''


def engineering_teaser():
    return f'''<section class="ce-home-section" id="collabrium-engineering" aria-labelledby="ce-home-title"><div class="wrap"><div class="ce-home-panel"><div><div class="eyebrow">Inside Collabrium / Backend engineering</div><h2 id="ce-home-title">The system behind<br>the screens.</h2><p>Explore the architecture, all 13 modules, connected workflows and the C# decisions that make the platform work.</p><a class="button" href="collabrium-engineering.html">Explore the backend {arrow('right')}</a></div><div class="ce-home-overview"><div class="ce-home-stats"><div><strong>4</strong><span>architecture layers</span></div><div><strong>31</strong><span>feature controllers</span></div><div><strong>13</strong><span>connected modules</span></div></div><div class="ce-home-topics"><a href="collabrium-engineering.html#system-map">Architecture &amp; CQRS {arrow('right')}</a><a href="collabrium-engineering.html#workflows">End-to-end workflows {arrow('right')}</a><a href="collabrium-engineering.html#integrations">SignalR, email &amp; workers {arrow('right')}</a><a href="collabrium-engineering.html#code-skills">Real code &amp; engineering skills {arrow('right')}</a></div></div></div></div></section>'''


def case_engineering_intro():
    return f'''<p>Explore the complete backend in a dedicated engineering walkthrough: all 13 functional areas, the four-project architecture, six connected workflows, work-item rules, layered access, persistence, SMTP/SignalR notifications, AI and reporting.</p><div class="ce-case-links"><a class="button" href="collabrium-engineering.html">Inside the backend {arrow('right')}</a><a class="text-link" href="collabrium-engineering.html#code-skills">Read the C# examples {arrow()}</a></div>'''


def engineering_page():
    sections = [
        ('system-map','01','System architecture','Four projects. Deliberate boundaries.', 'The API, use cases, business behavior and technical implementations have separate responsibilities. Project references point toward the application and domain core.', architecture_section()),
        ('modules','02','The complete platform','13 modules, connected by context.', 'Organization, delivery, learning, community and insights use the same tenant, people and project model. Open a module to inspect its capabilities and API surface.', module_catalog()),
        ('workflows','03','Connected workflows','Follow an operation through the backend.', 'Six implementation walkthroughs connect request handling, domain behavior, persistence and the effects that follow a saved change.', workflow_explorer()),
        ('domain-rules','04','Domain design','Business rules that change the outcome.', 'The model determines what a user can actually do with a project, sprint or work item. A status label alone does not make an operation valid.', domain_section()),
        ('security','05','Identity & access','The right user. The right scope.', 'Authentication is the entry point. Tenant membership, role/policy checks, project access and use-case rules define the resource boundary.', security_section()),
        ('data-api','06','Persistence & API design','Correct writes. Purposeful reads.', 'Database integrity, explicit models and consistent contracts support the workflows the product exposes.', data_section()),
        ('integrations','07','Real time, email & workers','Connect the saved work to the people.', 'Persistence, immediate updates, email templates, time-based processing and media storage each have a clear implementation boundary.', integration_section()),
        ('ai-reports','08','AI & reporting','Turn application data into useful guidance.', 'Structured suggestions and grounded insights sit alongside analytical queries and document generation.', ai_and_reports()),
        ('code-skills','09','C# in practice','The skills, visible in the code.', 'Open an example to see an exact excerpt and its source. These examples connect language features and design patterns to specific product behavior.', code_gallery()+skills_section()),
    ]
    nav=''.join(f'<a href="#{id}"><span>{n}</span>{name}</a>' for id,n,name,_,_,_ in sections)
    parts=''.join(f'<section class="ce-section" id="{id}" aria-labelledby="ce-title-{id}"><div class="ce-section-heading"><span class="label">{n} / {name}</span><h2 id="ce-title-{id}">{title}</h2><p>{intro}</p></div>{body}</section>' for id,n,name,title,intro,body in sections)
    body=f'''<main id="main" class="ce-page"><div class="wrap"><header class="ce-hero"><div class="breadcrumb"><a href="index.html#work">Selected work</a><span>/</span><a href="collabrium.html">Collabrium</a><span>/</span><span>Backend engineering</span></div><div class="eyebrow">Collabrium / Engineering walkthrough</div><h1>One platform.<br><em>Many connected decisions.</em></h1><p class="ce-hero-copy">A closer look at the .NET backend I helped lead and build: the architecture, business rules and connected workflows behind an integrated enterprise platform.</p><div class="ce-hero-actions"><a class="button" href="#system-map">Explore the architecture {arrow('down')}</a>{ext(REPO,'View the repository','text-link')}<a class="text-link" href="collabrium.html#demo">Watch the product {arrow()}</a></div><div class="ce-facts"><div><strong>290+</strong><span>HTTP API actions</span></div><div><strong>13</strong><span>functional areas</span></div><div><strong>3</strong><span>SignalR hubs</span></div><div><strong>10</strong><span>report types</span></div></div><p class="ce-ownership"><strong>My role:</strong> Team Lead &amp; Backend Developer · Four-person graduation project · PTUK, June 2026. Platform figures describe the shared project.</p></header><div class="ce-layout"><aside class="ce-toc"><nav aria-label="Backend walkthrough contents"><span class="label">Inside the backend</span>{nav}</nav><a class="ce-back" href="collabrium.html">Back to the project {arrow('left')}</a></aside><div class="ce-content">{parts}<div class="ce-review-note"><span class="label">Explore the evidence</span><p>Reviewed against the project README and implementation at commit <code>{SNAPSHOT[:7]}</code>. Source links are pinned to that snapshot.</p><div class="ce-sources">{source('README.md','Read the full README')}{ext('https://documenter.getpostman.com/view/27912762/2sBYHNX3rF/','API documentation','ce-source')}<a class="ce-source" href="collabrium.html#walkthrough">Explore the application screens {arrow()}</a></div></div></div></div></div></main>'''
    return document('Collabrium Backend Engineering — Raghad Hanon','Explore Collabrium’s .NET backend: all 13 modules, Clean Architecture, CQRS, domain workflows, tenant security, EF Core, SignalR, SMTP, Ollama AI and reports.',body,'collabrium-engineering.html').replace('</head>','<script src="collabrium-engineering.js" defer></script></head>')
