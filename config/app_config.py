STATUS_CHOICES = (
        ('Awaiting triage', 'Awaiting triage'),
        ('Being processed', 'Being processed'),
        ('Approved', 'Approved'),
        ('Not approved', 'Not approved'),
        ('On hold', 'On hold'),
        ('Closed', 'Closed'),
    )

TASK_CHOICES = (
        ('Scoping and costing', 'Scoping and costing'),
        ('Data retrieval and analysis', 'Data retrieval and analysis'),
        ('Approval', 'Approval'),
    )

PROJECT_TYPE_CHOICES = (
    ('Project', 'Project'),
    ('Request', 'Request')
)


DATA_TYPE_CHOICES = (
    ('Re-identifiable', 'Re-identifiable'),
    ('Aggregated', 'Aggregated')
)
