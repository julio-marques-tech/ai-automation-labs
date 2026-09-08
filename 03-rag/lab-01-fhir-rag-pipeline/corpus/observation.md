# FHIR v4.0.1 - Observation Resource

## Overview

The Observation resource represents "measurements and simple assertions made about a patient, device or other subject." This central healthcare element supports diagnosis, monitoring, baseline determination, and pattern recognition.

## Scope and Usage

Observations function as event resources within FHIR workflows. They typically consist of simple name/value pair assertions with metadata, though some observations group others logically or represent multi-component measurements.

### Common Uses

The specification lists these applications:

- Vital signs (body weight, blood pressure, temperature)
- Laboratory data (blood glucose, estimated GFR)
- Imaging results (bone density, fetal measurements)
- Clinical findings (abdominal tenderness)
- Device measurements (EKG, pulse oximetry)
- Assessment tools (APGAR, Glasgow Coma Score)
- Personal characteristics (eye color)
- Social history (tobacco use, family support)
- Core characteristics (pregnancy status, death assertions)

## Resource Status

- **Maturity Level**: N (Normative from v4.0.0)
- **Work Group**: Orders and Observations
- **Security Category**: Patient
- **Compartments**: Device, Encounter, Patient, Practitioner, RelatedPerson
- **ANSI Approval**: Yes

## Core Profile

The **Vital Signs profile** establishes minimum expectations for recording, searching, and retrieving vital sign observations associated with patients.

## Boundaries and Relationships

Observation serves measurements and point-in-time assessments. Other resources handle specialized contexts:

- **AllergyIntolerance**: Patient allergies
- **MedicationStatement**: Medications taken
- **FamilyMemberHistory**: Patient's family history
- **Procedure**: Procedure information
- **QuestionnaireResponse**: Questionnaire answers
- **Condition**: Clinical diagnoses
- **DiagnosticReport**: Complete clinical reports referencing Observations

The specification notes: "there will however be situations of overlap." Systems should consult implementer communities when uncertain about appropriate Observation usage.

## Resource Elements

### Primary Fields

| Element | Cardinality | Type | Description |
|---------|-------------|------|-------------|
| identifier | 0..* | Identifier | Business identifier for observation |
| basedOn | 0..* | Reference | Fulfills plan, proposal, or order |
| partOf | 0..* | Reference | Part of larger event |
| status | 1..1 | code | Result value status (registered, preliminary, final, amended) |
| category | 0..* | CodeableConcept | Observation type classification |
| code | 1..1 | CodeableConcept | What was observed |
| subject | 0..1 | Reference | Patient, group, device, or location |
| focus | 0..* | Reference | Actual observation focus when different from subject |
| encounter | 0..1 | Reference | Associated healthcare event |

### Temporal and Result Fields

| Element | Cardinality | Type | Description |
|---------|-------------|------|-------------|
| effective[x] | 0..1 | dateTime, Period, Timing, instant | Physiologically relevant time |
| issued | 0..1 | instant | Result availability timestamp |
| performer | 0..* | Reference | Who asserted the observation |
| value[x] | 0..1 | Multiple types | Actual result (Quantity, CodeableConcept, string, boolean, integer, Range, Ratio, SampledData, time, dateTime, Period) |
| dataAbsentReason | 0..1 | CodeableConcept | Why value is missing |

### Interpretation and Context

| Element | Cardinality | Type | Description |
|---------|-------------|------|-------------|
| interpretation | 0..* | CodeableConcept | High, low, normal assessment |
| note | 0..* | Annotation | Comments about observation |
| bodySite | 0..1 | CodeableConcept | Observed body part |
| method | 0..1 | CodeableConcept | Observation mechanism |
| specimen | 0..1 | Reference | Specimen used |
| device | 0..1 | Reference | Measurement device |

### Reference Ranges and Related Data

| Element | Cardinality | Type | Description |
|---------|-------------|------|-------------|
| referenceRange | 0..* | BackboneElement | Interpretation guidance with low, high, type, appliesTo, age, text |
| hasMember | 0..* | Reference | Group observation members |
| derivedFrom | 0..* | Reference | Measurement sources |
| component | 0..* | BackboneElement | Multi-component observations |

### Components

Components share the same attributes as parent observations, with their own code, value[x], dataAbsentReason, interpretation, and referenceRange elements.

## Constraints

- dataAbsentReason SHALL only appear if value[x] is absent
- If Observation.code matches component.code, the parent value element SHALL NOT be present
- referenceRange requires at least low, high, or text

## Related Resources

The specification indicates Observation is referenced by: AdverseEvent, Appointment, CarePlan, ChargeItem, ClinicalImpression, Communication, CommunicationRequest, Condition, Contract, DeviceRequest, DeviceUseStatement, DiagnosticReport, Encounter, FamilyMemberHistory, Goal, GuidanceResponse, ImagingStudy, Immunization, MedicationAdministration, MedicationRequest, MedicationStatement, MolecularSequence, Procedure, QuestionnaireResponse, RequestGroup, RiskAssessment, ServiceRequest, and SupplyRequest.

Source: https://hl7.org/fhir/R4/observation.html
