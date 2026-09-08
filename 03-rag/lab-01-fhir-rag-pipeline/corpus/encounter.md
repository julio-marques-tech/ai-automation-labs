# Encounter - FHIR v4.0.1

## Overview

The Encounter resource represents "an interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient."

## Scope and Usage

Patient encounters are characterized by their setting, including ambulatory, emergency, home health, inpatient, and virtual encounters. An Encounter encompasses the complete lifecycle from pre-admission through admission, stay, and discharge for inpatient cases. During encounters, patients may move between practitioners and locations.

The broad scope means not all elements apply universally. Admission/discharge information is maintained in a separate Hospitalization component. The `class` element distinguishes between settings and guides validation and business rule application.

There is significant variance across organizations regarding which business events trigger a new Encounter or what aggregation level is used. A single practitioner visit during hospitalization might create a new Encounter instance, or it might aggregate into a single encounter for the entire hospitalization. Encounters can be grouped under other Encounters using the `partOf` element.

Encounter instances may exist before actual service delivery, using `status: 'planned'` to convey pre-admission information including planned start dates and locations.

The Hospitalization component stores extended hospitalization-related information, maintaining the same period as the encounter itself. When periods differ, separate encounter instances should be created as `partOf` relationships.

### Status Management

Encounters progress through multiple statuses during their lifecycle, typically: planned, in-progress, finished/cancelled. A `statusHistory` component tracks these transitions without requiring resource version scanning.

There is no direct indication from status alone whether an encounter is "admitted." Context, business practices, policies, workflows, and encounter types influence this definition. Statuses like "arrived," "triaged," or "in progress" may signal admission start, often accompanied by the hospitalization sub-component. The "on leave" status may or may not constitute admission depending on circumstances.

At minimum, a patient is considered admitted when status is "in-progress."

## Boundaries and Relationships

The Encounter resource differs from the Appointment resource. Appointments establish scheduled dates; Encounters document actual service provision when patients appear. An encounter in "planned" status precedes the actual occurrence, with expectation of progression to completion.

Appointments are typically used for planning and scheduling. Once an appointment approaches start time and is fulfilled, it links to a newly created encounter, which may begin in "arrived" status upon admission.

Communication resources document simultaneous practitioner-patient interactions without direct contact (phone messages, correspondence), containing sent/received times but no duration.

## Resource Elements

### Core Identifier and Status

- **identifier** (0..*): Identifier(s) by which this encounter is known
- **status** (1..1, required): Current state - planned | arrived | triaged | in-progress | onleave | finished | cancelled +
- **statusHistory** (0..*): List of past encounter statuses, each containing:
  - **status** (1..1, required): Previous status value
  - **period** (1..1, required): Time in specified status

### Classification

- **class** (1..1, required): Classification of patient encounter (ambulatory, inpatient, emergency, home health)
- **classHistory** (0..*): Tracking of encounter transitions without resource history scanning, each containing:
  - **class** (1..1, required): Previous classification
  - **period** (1..1, required): Time in specified class

### Encounter Type and Service

- **type** (0..*): Specific encounter type (e-mail consultation, surgical day-care, skilled nursing, rehabilitation)
- **serviceType** (0..1): Broad service categorization (e.g., cardiology)
- **priority** (0..1): Urgency indication

### Participants and Subject

- **subject** (0..1): Patient or group present at encounter
- **episodeOfCare** (0..*): Episode(s) of care classification
- **basedOn** (0..*): ServiceRequest that initiated this encounter
- **participant** (0..*): People responsible for providing service, each containing:
  - **type** (0..*): Role of participant
  - **period** (0..1): Participation time period
  - **individual** (0..1): Practitioner, PractitionerRole, or RelatedPerson reference

### Appointment and Timing

- **appointment** (0..*): Appointment(s) that scheduled this encounter
- **period** (0..1): Encounter start and end time
- **length** (0..1): Encounter duration, excluding leave periods

### Reason and Diagnosis

- **reasonCode** (0..*): Coded reason for encounter (can be admission diagnosis)
- **reasonReference** (0..*): Reason expressed through references to Condition, Procedure, Observation, or ImmunizationRecommendation
- **diagnosis** (0..*): Diagnoses relevant to this encounter, each containing:
  - **condition** (1..1, required): Condition or Procedure reference
  - **use** (0..1): Role within encounter (admission, billing, discharge)
  - **rank** (0..1): Diagnosis ranking for each role type

### Billing and Provider

- **account** (0..*): Accounts usable for billing
- **serviceProvider** (0..1): Organization primarily responsible for encounter services

### Hospitalization Details

- **hospitalization** (0..1): Admission-related information containing:
  - **preAdmissionIdentifier** (0..1): Pre-admission identifier
  - **origin** (0..1): Location/organization from which patient came
  - **admitSource** (0..1): Admission source (physician referral, transfer)
  - **reAdmission** (0..1): Readmission status and reason
  - **dietPreference** (0..*): Patient-reported diet preferences
  - **specialCourtesy** (0..*): VIP, board member status
  - **specialArrangement** (0..*): Special requests (wheelchair, translator, stretcher)
  - **destination** (0..1): Discharge location/organization
  - **dischargeDisposition** (0..1): Post-discharge location category

### Location Tracking

- **location** (0..*): Locations where patient has been, each containing:
  - **location** (1..1, required): Location reference
  - **status** (0..1): Participant presence status (planned | active | reserved | completed)
  - **physicalType** (0..1): Location hierarchy level (bed/room/ward)
  - **period** (0..1): Time present at location

### Relationships

- **partOf** (0..1): Another Encounter this encounter is part of (administratively or temporally)

Source: https://hl7.org/fhir/R4/encounter.html
